from bisect import bisect as bs
t = [0] * int(input())
a = sorted(map(int, input().split()))
def g(x): return a[bs(a, x) - 1] == x


for _, x in enumerate(a):
    for i in range(31):
        l = x - 2 ** i
        r = x + 2 ** i
        t[_] = max(t[_], g(l) + g(r))
m = max(t)
if m == 2:
    print(3)
    _ = t.index(2)
    x = a[_]
    for i in range(31):
        l = x - 2 ** i
        r = x + 2 ** i
        if g(l) and g(r):
            print(l, x, r)
            return
if m == 1:
    print(2)
    _ = t.index(1)
    x = a[_]
    for i in range(31):
        l = x - 2 ** i
        r = x + 2 ** i
        if g(l):
            print(l, x)
            return
        if g(r):
            print(x, r)
            return
print(1)
print(a[0])
