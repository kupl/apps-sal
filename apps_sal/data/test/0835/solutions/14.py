def f(x):
    return max(0, ham[0] * x - nb) * pb + max(0, ham[1] * x - ns) * ps + max(0, ham[2] * x - nc) * pc


s = input()
(nb, ns, nc) = list(map(int, input().split()))
(pb, ps, pc) = list(map(int, input().split()))
r = int(input())
ham = (s.count('B'), s.count('S'), s.count('C'))
hi = 2 ** 64
lo = 0
while hi - lo > 1:
    m = (hi + lo) // 2
    t = f(m)
    if t <= r:
        lo = m
    else:
        hi = m
print(lo)
