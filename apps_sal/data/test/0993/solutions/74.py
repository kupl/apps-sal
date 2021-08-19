from collections import Counter
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = Counter()
sm = 0
c[sm] += 1
for i in range(n):
    sm += a[i]
    c[sm % m] += 1
ans = 0
for v in list(c.values()):
    ans += v * (v - 1) // 2
print(ans)
