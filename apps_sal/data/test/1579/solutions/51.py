import sys
sys.setrecursionlimit(100000)


def solve(x, x_set, y_set, x2y, y2x):
    num_e = 0
    if x in x2y:
        x_set.add(x)
        yl = x2y.pop(x)
        num_e += len(yl)
        for y in yl:
            num_e += solve(y, y_set, x_set, y2x, x2y)
    return num_e


N = int(input())
X2Y = {}
Y2X = {}
for i in range(N):
    (x, y) = map(int, input().split())
    if x in X2Y:
        X2Y[x].append(y)
    else:
        X2Y[x] = [y]
    if y in Y2X:
        Y2X[y].append(x)
    else:
        Y2X[y] = [x]
ans = 0
while X2Y:
    x = next(iter(X2Y))
    x_set = set()
    y_set = set()
    num_e = solve(x, x_set, y_set, X2Y, Y2X)
    ans += len(x_set) * len(y_set) - num_e // 2
print(ans)
