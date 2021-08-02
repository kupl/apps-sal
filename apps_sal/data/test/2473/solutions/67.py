from itertools import accumulate
n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]
X, Y = zip(*XY)


def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i + 1 for i, e in enumerate(XS)}


Xlabel = compress(X)
Ylabel = compress(Y)
rX = {j: i for i, j in Xlabel.items()}
rY = {j: i for i, j in Ylabel.items()}
lX = len(Xlabel)
lY = len(Ylabel)
F = [[0] * (lX + 1) for _ in range(lY + 1)]
for x, y in XY:
    F[Ylabel[y]][Xlabel[x]] = 1
for i in range(lY):
    F[i + 1] = list(accumulate(F[i + 1]))
F = list(zip(*F))
for j in range(lY):
    F[j + 1] = list(accumulate(F[j + 1]))
F = list(zip(*F))
ans = float("inf")
for y1 in range(lY):
    for y2 in range(y1 + 1, lY + 1):
        for x1 in range(lX):
            for x2 in range(x1 + 1, lX + 1):
                count = F[y2][x2] - F[y1][x2] - F[y2][x1] + F[y1][x1]
                if count >= k:
                    temp = (rX[x2] - rX[x1 + 1]) * (rY[y2] - rY[y1 + 1])
                    ans = min(ans, temp)
print(ans)
