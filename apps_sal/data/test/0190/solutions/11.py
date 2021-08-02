z = input().split()
a = []
for i in range(2):
    a.append(int(z[i]))
n = a[0]
m = a[1]
b = []
x1 = 1001
x2 = 0
y1 = 1001
y2 = 0
for i in range(n):
    b.append(str(input()))
for i in range(n):
    for j in range(m):
        if b[i][j] == '*':
            if i < y1:
                y1 = i
            if j < x1:
                x1 = j
            if i > y2:
                y2 = i
            if j > x2:
                x2 = j
x = x2 - x1 + 1
y = y2 - y1 + 1
if x > y:
    print(x)
else:
    print(y)
