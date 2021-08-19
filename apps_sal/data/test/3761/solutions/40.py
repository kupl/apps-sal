import sys
MOD = 10 ** 9 + 7
INF = float('inf')
S = input()
(X, Y) = list(map(int, input().split()))
x_num = []
y_num = []
f = 0
axis = 0
count = 0
for s in S:
    if s == 'F':
        count += 1
    else:
        if count > 0:
            if axis == 0:
                if f == 0:
                    X -= count
                else:
                    x_num.append(count)
            else:
                y_num.append(count)
            count = 0
        f = 1
        axis = (axis + 1) % 2
if count > 0:
    if axis == 0:
        if f == 0:
            X -= count
        else:
            x_num.append(count)
    else:
        y_num.append(count)
x_num.sort(reverse=True)
y_num.sort(reverse=True)
xs = X
for x in x_num:
    if xs >= 0:
        xs -= x
    else:
        xs += x
ys = Y
for y in y_num:
    if ys >= 0:
        ys -= y
    else:
        ys += y
if xs == 0 and ys == 0:
    print('Yes')
else:
    print('No')
