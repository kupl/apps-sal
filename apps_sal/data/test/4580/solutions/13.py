a = int(input())
b = list(map(int, input().split()))
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
x = 0
for z in range(a):
    if b[z] <= 399:
        c = c + 1
    if 400 <= b[z] < 799:
        d = d + 1
    if 800 <= b[z] <= 1199:
        e = e + 1
    if 1200 <= b[z] <= 1599:
        f = f + 1
    if 1600 <= b[z] <= 1999:
        g = g + 1
    if 2000 <= b[z] <= 2399:
        h = h + 1
    if 2400 <= b[z] <= 2799:
        i = i + 1
    if 2800 <= b[z] <= 3199:
        j = j + 1
    if b[z] >= 3200:
        k = k + 1
if c != 0:
    x = x + 1
if d != 0:
    x = x + 1
if e != 0:
    x = x + 1
if f != 0:
    x = x + 1
if g != 0:
    x = x + 1
if h != 0:
    x = x + 1
if i != 0:
    x = x + 1
if j != 0:
    x = x + 1
if k + x > a:
    print(x, a)
elif (c + d + e + f + g + h + i + j) == 0 and k != 0:
    print(1, k)
else:
    print(x, k + x)
