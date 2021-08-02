n = int(input())
a = [[0, 0]]
xpos = 0
xneg = 0
for i in range(n):
    x, y = input().split(' ')
    a.append([int(x), int(y)])
    if int(x) < 0:
        xneg += 1
    else:
        xpos += 1
a.sort()
m = a.index([0, 0])
if xpos > xneg:
    l = 0
    h = m + xneg + 2
elif xneg > xpos:
    l = m - xpos - 1
    h = n + 1
else:
    l = 0
    h = n + 1
s = 0
for i in range(l, h):
    s += a[i][1]
print(s)
