def f(l): return map(int, l.split())


N, K = f((p := input)())
c = [0] * (l := 10**5 + 1)
s = 0
for i in (r := range)(N):
    a, b = f(p())
    c[a] += b
for i in r(l):
    s += c[i]
    if s >= K:
        print(i)
        break
