def f(arr):
    d = max(arr)
    for i in range(len(arr)):
        arr[i] = d - arr[i]


# for _ in range(1):
for _ in range(int(input())):
    # n, k = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    i = n - 1
    ans = 0
    while i > 0:
        if arr[i - 1] <= arr[i]:
            i -= 1
            continue
        ans += arr[i - 1] - arr[i]
        i -= 1
    print(ans)
