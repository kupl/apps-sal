(n, m) = map(int, input().split())
field = [input() for _ in range(n)]
black = 0
minheight = minwidth = 101
maxheight = maxwidth = 0
for i in range(n):
    s = field[i]
    for j in range(m):
        if s[j] == 'B':
            black += 1
            minheight = min(i, minheight)
            maxheight = max(i, maxheight)
            minwidth = min(j, minwidth)
            maxwidth = max(j, maxwidth)
if black == 0:
    print(1)
else:
    a = maxwidth - minwidth + 1
    b = maxheight - minheight + 1
    c = max(a, b)
    des = c * c
    if des > n * m or c > n or c > m:
        print(-1)
    else:
        print(des - black)
