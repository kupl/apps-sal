def solve():
    (n, x) = list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    max_val = 0
    dp1 = [0] * (n + 1)
    for i in range(1, n + 1):
        dp1[i] = max(dp1[i - 1] + a[i], a[i])
        max_val = max(max_val, dp1[i])
    dp2 = [0] * (n + 1)
    for i in range(1, n + 1):
        dp2[i] = max(dp1[i - 1] + a[i] * x, dp2[i - 1] + a[i] * x, a[i] * x)
        max_val = max(max_val, dp2[i])
    dp3 = [0] * (n + 1)
    for i in range(1, n + 1):
        dp3[i] = max(dp2[i - 1] + a[i], dp3[i - 1] + a[i], a[i])
        max_val = max(max_val, dp3[i])
    print(max_val)


solve()
