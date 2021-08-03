import sys


# 一つ前の座標と、方向を返す
def f(x, y, i):
    d = 1 << i
    if y > x and y > -x:
        return x, y - d, "U"
    elif y < x and y > -x:
        return x - d, y, "R"
    elif y < x and y < -x:
        return x, y + d, "D"
    else:
        return x + d, y, "L"


N = int(input())
X = []
Y = []
mx = 0
for i in range(N):
    x, y = [int(x) for x in input().split()]
    mx = max(abs(x) + abs(y), mx)
    X.append(x)
    Y.append(y)

s = (X[0] + Y[0]) % 2
for i in range(N):
    if s != (X[i] + Y[i]) % 2:
        print((-1))
        return

# s == 1 のとき：D:[1,2,4,8,...]
# s == 0 のとき：D:[1,1,2,4,8,...]

if s == 0:
    X = [x - 1 for x in X]

D = []
d = 1
while d < mx:
    D.append(d)
    d = d * 2

m = len(D)
print((m if s != 0 else m + 1))
if s == 0:
    D = [1] + D
print((" ".join([str(d) for d in D])))

for i in range(N):
    x, y = X[i], Y[i]
    dirs = []
    for j in range(m - 1, -1, -1):
        x, y, dir = f(x, y, j)
        dirs.append(dir)
    if s == 0:
        dirs.append("R")
    print(("".join(dirs[::-1])))
