__author__ = 'valeriy.shevchuk'

input()
b = sorted(list(map(int, input().split())))
input()
g = sorted(list(map(int, input().split())))

c = 0
while b and g:
    bb = b[0]
    gg = g[0]
    if abs(bb - gg) <= 1:
        c += 1
        b.pop(0)
        g.pop(0)
    else:
        b.pop(0) if bb < gg else g.pop(0)

print(c)
