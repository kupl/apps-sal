from scipy.optimize import fmin
l = [list(map(int, input().split()))for i in range(int(input()))]


def g(s):
    a, b = s
    d = 0
    for i, j in l:
        d = max(d, (i - a)**2 + (j - b)**2)
    return d


x, y = fmin(g, [500, 500], ftol=10**-7, disp=0)
print(g((x, y))**0.5)
