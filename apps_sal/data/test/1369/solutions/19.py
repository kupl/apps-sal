from scipy.optimize import fmin
n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))


def calc(k):
    i, j = k
    return max((x - i)**2 + (y - j)**2 for x, y in xy)


x, y = fmin(calc, [500, 500], disp=0)

print(calc([x, y])**0.5)
