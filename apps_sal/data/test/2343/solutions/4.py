case = int(input())
for i in range(case):
    f = [0] * 32
    g = [0] * 32
    success = False
    n, k = map(int, input().split())
    ans = n
    for i in range(1, n):
        f[i] = f[i - 1] * 4 + 1
        if f[i] >= k:
            success = True
            break
    for i in range(1, n + 1):
        if k < (1 << i) - 1:
            break
        k = k - (1 << i) + 1
        ans = ans - 1
    for i in range(n - 1, ans - 1, -1):
        if i >= 32 or (i and f[i] == 0):
            success = True
            break
        g[i] = 1 if i == n - 1 else g[i + 1] * 2 + 3
        k = k - f[i] * g[i]
        if k <= 0:
            success = True
            break
    print("YES %d" % ans if success else "NO")
