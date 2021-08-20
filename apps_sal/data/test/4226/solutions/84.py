(x, y) = map(int, input().split())
l = []
flag = False
for i in range(x + 1):
    l.append((i, x - i))
for (xx, yy) in l:
    if y == xx * 2 + yy * 4:
        flag = True
        break
if flag:
    print('Yes')
else:
    print('No')
