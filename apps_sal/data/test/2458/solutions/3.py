3
MOD = 1000000007
(t, k) = map(int, input().split())
(a, b) = ([], [])
for i in range(t):
    (_a, _b) = map(int, input().split())
    a.append(_a)
    b.append(_b)
upper = max(b) + 1
way = [1]
sum_way = [1]
for i in range(1, upper):
    way.append((way[i - 1] + (way[i - k] if i >= k else 0)) % MOD)
    sum_way.append((sum_way[i - 1] + way[i]) % MOD)
for i in range(t):
    print((sum_way[b[i]] - sum_way[a[i] - 1]) % MOD)
