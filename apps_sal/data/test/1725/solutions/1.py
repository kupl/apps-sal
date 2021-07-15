def f(t):
    t.sort()
    return t[len(t) // 2]
    
n, m, d = map(int, input().split())
t, p = [], [0] * (n * m)
for i in range(n):
    t += list(map(int, input().split()))
u = t[0] % d
for i, v in enumerate(t):
    if u != v % d:
        p = []
        break
    else: p[i] = v // d
if p:
    s = f(p)
    print(sum(abs(i - s) for i in p))
else: print(-1)
