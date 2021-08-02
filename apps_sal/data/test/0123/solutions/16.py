def I(): return list(map(int, input().split()))


n, k = I()
a, b = list(I()), list(I())
if k == 1:
    c = list(a)
    c[c.index(0)] = b[0]
    if sorted(c) == c:
        print('No')
        return
print('Yes')
