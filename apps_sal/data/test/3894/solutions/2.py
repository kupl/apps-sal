def f():
    return map(int, input().split())


(n, k) = f()
s = 0
for a in f():
    d = 0
    while a & 1 << d == 0:
        d += 1
    t = (a == 3 << d) ^ d & 1
    x = a & 1 if a < 4 else 0 if a & 1 else 2 - t
    y = a if a < 3 else a & 1 ^ 1
    s ^= x if k & 1 else y
print('Kevin' if s else 'Nicky')
