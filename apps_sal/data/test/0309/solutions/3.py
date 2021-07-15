l, r = map(int, input().split())
i = 0
if l == r: print(0)
else:
    l, r = format(l, 'b'), format(r, 'b')
    if len(l) == len(r):
        while l[i] == r[i]: i += 1
    print((1 << len(r) - i) - 1)
