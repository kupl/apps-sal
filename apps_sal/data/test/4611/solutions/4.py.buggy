n = int(input())
xx = 0
yy = 0
tt = 0
for i in range(n):
    t, x, y = map(int, input().split())
    d = abs(xx - x) + abs(yy - y)
    if t - tt < d or (t - tt - d) % 2 == 1:
        print('No')
        return
    xx = x
    yy = y
    tt = t
print('Yes')
