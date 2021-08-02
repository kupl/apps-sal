
tt = int(input())

for loop in range(tt):

    n, k = map(int, input().split())
    s = input()

    lis = [0] * n
    tmp = [0] * n
    now = 0

    for i in range(n):

        if s[i] == "1":
            now += 1

            if i + k < n:
                tmp[i + k] += 1

        lis[i] += now

        now -= tmp[i]

    tmp = [0] * n
    now = 0

    for i in range(n - 1, -1, -1):

        if s[i] == "1":
            now += 1

            if i - k >= 0:
                tmp[i - k] += 1

        lis[i] += now
        now -= tmp[i]

    tmp = -1
    ans = 0
    for i in range(n):

        if tmp < 0 and lis[i] == 0:
            ans += 1
            tmp = k

        tmp -= 1

    print(ans)
