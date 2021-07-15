__author__ = 'Данила'
n, m = map(int, input().split())
l = []
for i in range(m):
    d, h = map(int, input().split())
    l.append((d, h))
k = - 1
flag = True
for i in range(m - 1):
    b = l[i + 1][1]
    a = l[i][1]
    y = l[i + 1][0]
    x = l[i][0]
    if a + y - x >= b and a - y + x <= b:
        if (y - x - a + b)//2 >= b - a:
            k1 = (y - x - a + b)//2 + a
            if k1 > k:
                k = k1
        else:
            k1 = max(a, b)
            if k1 > k:
                k = k1
    else:
        flag = False

b = l[0][0] - 1 + l[0][1]
a = l[-1][1] + n - l[-1][0]
if flag:
    print(max(k, a, b))
else:
    print('IMPOSSIBLE')
