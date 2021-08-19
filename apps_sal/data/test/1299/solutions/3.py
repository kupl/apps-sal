(n, k) = list(map(int, input().split()))
v = list(map(int, input().split()))
(s, dp) = ([0 for i in range(0, n)], [0 for i in range(0, n)])
(sol, a, b) = (0, 0, 0)
for i in range(n - 1, -1, -1):
    s[i] = v[i]
    if i + 1 < n:
        s[i] += s[i + 1]
    if i + k < n:
        s[i] -= v[i + k]
    dp[i] = s[i]
    if i + 1 < n:
        dp[i] = max(dp[i], dp[i + 1])
for i in range(0, n):
    if i + k > n - 1:
        break
    if s[i] + dp[i + k] > sol:
        sol = s[i] + dp[i + k]
        a = i
for b in range(a + k, n):
    if b + k > n - 1:
        break
    if s[a] + s[b] == sol:
        break
print(a + 1, b + 1)
