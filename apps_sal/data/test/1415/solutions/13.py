__author__ = 'Utena'
(x, y, x0, y0) = list(map(int, input().split()))
x1 = x0
y1 = y0
s = list(input())
k = 0
l = []
l1 = [[x0, y0]]
l2 = [[0] * (y + 1) for i in range(x + 1)]
for i in s:
    if i == 'R' and y0 < y:
        y0 += 1
        l1.append([x0, y0])
    elif i == 'L' and y0 > 1:
        y0 -= 1
        l1.append([x0, y0])
    elif i == 'U' and x0 > 1:
        x0 -= 1
        l1.append([x0, y0])
    elif i == 'D' and x0 < x:
        x0 += 1
        l1.append([x0, y0])
    else:
        l1.append([x0, y0])
for j in range(len(s)):
    x1 = l1[j][0]
    y1 = l1[j][1]
    l2[x1][y1] += 1
    if l2[x1][y1] > 1:
        l.append('0')
    else:
        l.append('1')
        k += 1
print(' '.join(l) + ' %d' % (x * y - k))
