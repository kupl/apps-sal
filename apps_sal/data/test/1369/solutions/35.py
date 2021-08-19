from scipy.optimize import fmin
n = int(input())
l = []
for i in range(n):
    (x, y) = [int(j) for j in input().split()]
    l.append((x, y))


def f(s):
    (x, y) = s
    maxi = 0
    for (i, j) in l:
        maxi = max(maxi, (i - x) ** 2 + (j - y) ** 2)
    return maxi


(x, y) = fmin(f, [100, 100], xtol=10 ** (-9), disp=0)
ans = f((x, y)) ** 0.5
print(ans)
