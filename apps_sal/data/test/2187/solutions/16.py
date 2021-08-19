t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]
    ans = 0
    ind = n - 2
    while ind != -1:
        while ind != -1 and arr[ind] <= arr[ind + 1]:
            ind -= 1
        if ind != -1:
            ans += arr[ind] - arr[ind + 1]
            arr[ind + 1] = arr[ind]
    print(ans)
