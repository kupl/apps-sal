def f():
    return map(int, input().split())


(n, k) = f()
(s, d) = ([], -1)
for q in f():
    if q < 0:
        k -= 1
        if d > 0:
            s += [d]
        d = 0
    elif d + 1:
        d += 1
s.sort()


def g(k, d):
    d += len(s) << 1
    for q in s:
        if q > k:
            break
        k -= q
        d -= 2
    return d


print(0 if d < 0 else -1 if k < 0 else g(k, 2) if k < d else min(g(k, 2), g(k - d, 1)))
