n = int(input())
seq = list(map(int, input().split(" ")))

if sum(seq) < 3 or sum(seq) == 5:
    print(-1)

else:
    arr = [0, 0, 0, 0, 0]
    for s in seq:
        arr[s] += 1

    ans = 0
    if arr[2] >= arr[1]:
        ans += arr[1]
        arr[2] -= arr[1]
        arr[3] += arr[1]
        arr[1] = 0
    else:
        ans += arr[2]
        arr[1] -= arr[2]
        arr[3] += arr[2]
        arr[2] = 0

    ans += 2 * (arr[1] // 3)
    arr[3] += arr[1] // 3
    arr[1] %= 3

    if (arr[3] >= arr[1]):
        ans += arr[1]
        arr[4] += arr[1]
        arr[3] -= arr[1]
        arr[1] = 0
    else:
        if arr[1] < 2:
            ans += arr[3]
            arr[4] += arr[3]
            arr[1] -= arr[3]
            arr[3] = 0

    if arr[1] > 0:
        if arr[1] == 2:
            ans += arr[1]
            arr[4] -= 1
            arr[3] += 2
            arr[1] = 0
        else:
            ans += 2
            arr[4] -= 2
            arr[3] += 2
            arr[1] = 0

    ans += 2 * (arr[2] // 3)
    arr[3] += 2 * (arr[2] // 3)
    arr[2] %= 3

    if arr[2] > 0:
        if (arr[4] >= arr[2]):
            ans += arr[2]
            arr[4] -= arr[2]
            arr[3] += 2 * arr[2]
            arr[2] = 0

            ans += 2 * (arr[2])
            arr[4] += 2 * arr[2]
            arr[3] -= arr[2]
            arr[2] = 0
        else:
            if (arr[4] > 0):
                ans += arr[2]
                arr[4] -= arr[2]
                arr[3] += 2 * arr[2]
                arr[2] = 0
            else:
                if arr[2] == 1:
                    ans += 2 * arr[2]
                    arr[3] += 2
                    arr[2] = 0
                else:
                    ans += arr[2]
                    arr[4] += 1
                    arr[2] = 0

    print(ans)
