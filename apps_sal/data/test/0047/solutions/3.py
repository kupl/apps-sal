(n, x) = map(int, input().split())
dp1 = [0] * n
dp2 = [0] * n
dp0 = [0] * n
ans = 0
v = [int(i) for i in input().split()]
dp0[0] = max(0, v[0])
dp1[0] = v[0] * x
i = 0
ans = max(ans, dp1[i], dp2[i], dp0[i])
for i in range(1, n):
    dp0[i] = max(0, dp0[i - 1] + v[i])
    dp1[i] = max(dp1[i - 1] + v[i] * x, dp0[i - 1] + v[i] * x)
    dp2[i] = max(dp1[i - 1] + v[i], dp2[i - 1] + v[i])
    ans = max(ans, dp1[i], dp2[i], dp0[i])
print(ans)
