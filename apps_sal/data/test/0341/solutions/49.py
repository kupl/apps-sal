(n, k) = list(map(int, input().split()))
(r, s, p) = list(map(int, input().split()))
t = input()
tt = list(t)
d = {'r': p, 's': r, 'p': s}
dp = [d[t[i]] for i in range(n)]
for i in range(n - k):
    if tt[i] == tt[i + k]:
        dp[i + k] = 0
        tt[i + k] = 'x'
print(sum(dp))
