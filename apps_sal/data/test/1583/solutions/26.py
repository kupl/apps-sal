from math import tan, atan2, pi, degrees


def f(theta):
    if theta < thres:
        return V - a ** 3 * tan(theta) / 2
    else:
        return a * b * b / tan(theta) / 2


eps = 1e-9
a, b, x = list(map(int, input().split()))
V = a * a * b
thres = atan2(b, a)

bad, good = pi / 2, 0
while bad - good > eps:
    mid = (bad + good) / 2
    if f(mid) >= x:
        good = mid
    else:
        bad = mid
print((degrees(good)))

