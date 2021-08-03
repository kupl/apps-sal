def f(): return map(int, input().split())


n, k = f()
s, d = [], -1
for q in f():
    if q < 0:
        k -= 1
        if d > 0:
            s += [d]
        d = 0
    elif d > -1:
        d += 1
s.sort()
t = 2 * len(s)
for q in s:
    if q > k:
        break
    k -= q
    t -= 2
print(-1 if k < 0 else 0 if d < 0 else 2 + t - (k >= d))
