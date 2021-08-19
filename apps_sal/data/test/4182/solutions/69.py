(n, m, x, y) = list(map(int, input().split()))
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))
xmax = max(xl)
ymin = min(yl)
isWar = True
for i in range(x + 1, y + 1):
    if xmax < i and ymin >= i:
        isWar = False
        break
if isWar:
    print('War')
else:
    print('No War')
