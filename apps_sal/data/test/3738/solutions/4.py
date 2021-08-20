import operator
table = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
(a, b) = list(map(int, input().split()))
s = list(input())
zs = set()
(x, y) = (0, 0)
zs.add((x, y))
for c in s:
    (x, y) = list(map(operator.add, (x, y), table[c]))
    zs.add((x, y))
result = False
for (zx, zy) in zs:
    (p, q) = (a - zx, b - zy)
    if x == 0 and p != 0 or (x != 0 and p % x != 0) or (x != 0 and p // x < 0):
        continue
    if y == 0 and q != 0 or (y != 0 and q % y != 0) or (y != 0 and q // y < 0):
        continue
    if x != 0 and y != 0 and (p // x != q // y):
        continue
    result = True
print('Yes' if result else 'No')
