from scipy.optimize import fmin
N = int(input())

INF = 10 ** 18
fixed_x = [INF, -INF]
R = [INF, -INF]
L = [INF, -INF]
fixed_y = [INF, -INF]
U = [INF, -INF]
D = [INF, -INF]


def update(fixed, li, x, y):
    li[0], li[1] = min(li[0], x), max(li[1], x)
    fixed[0], fixed[1] = min(fixed[0], y), max(fixed[1], y)


for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    if d == 'L':
        update(fixed_y, L, x, y)
    elif d == 'R':
        update(fixed_y, R, x, y)
    elif d == 'U':
        update(fixed_x, U, y, x)
    else:
        update(fixed_x, D, y, x)


def calc_x(t, fixed, dec, inc):
    left = INF
    right = -INF
    for li, speed in [(fixed, 0), (dec, -1), (inc, 1)]:
        left = min(left, li[0] + speed * t)
        right = max(right, li[1] + speed * t)
    return right - left


def area(t):
    if t < 0:
        return INF
    return calc_x(t, fixed_x, L, R) * calc_x(t, fixed_y, D, U)


xopt = fmin(area, x0=10**8, ftol=10**-9, disp=False)
answer = area(xopt[0])
print(answer)
