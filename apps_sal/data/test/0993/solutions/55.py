from collections import Counter
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = Counter()
s = 0
c[s] += 1
for i in range(n):
    s += a[i]
    c[s % m] += 1
ans = 0
for v in list(c.values()):
    ans += v * (v - 1) // 2
print(ans)
