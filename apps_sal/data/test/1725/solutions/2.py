n, m, d = map(int, input().split())
k, t = n * m, []
for i in range(n):
    t += list(map(int, input().split()))
u = t[0] % d
for v in t:
    if u != v % d:
        t = []
        break
if t:
    t.sort()
    s = t[k // 2]
    print(sum(abs(v - s) for v in t) // d)
else: print(-1)
