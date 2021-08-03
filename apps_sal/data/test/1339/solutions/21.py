n = int(input())
l = []
mi, ma = 11**11, 0
for _ in range(n):
    x, y = map(int, input().split())
    if x < mi:
        mi = x
    if y > ma:
        ma = y
    l += [(x, y)]
if (mi, ma) in l:
    print(l.index((mi, ma)) + 1)
else:
    print(-1)
