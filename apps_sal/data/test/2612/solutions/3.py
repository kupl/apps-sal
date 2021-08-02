t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(1, n + 1):
        ans[i - 1] = max(ans[i - 1], 1)
        for j in range(2, n // i + 1):
            if a[i * j - 1] > a[i - 1]:
                ans[i * j - 1] = max(ans[i * j - 1], ans[i - 1] + 1)
    print(max(ans))
