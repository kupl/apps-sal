from scipy.optimize import fmin

N = int(input())

INF = 10 ** 18

X, Y = [[], [], []], [[], [], []]
for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)

    if d == "R":
        X[0].append(x)
    elif d == "L":
        X[1].append(x)
    else:
        X[2].append(x)

    if d == "U":
        Y[0].append(y)
    elif d == "D":
        Y[1].append(y)
    else:
        Y[2].append(y)

for i in range(3):
    X[i] = [min(X[i] + [INF]), max(X[i] + [-INF])]
    Y[i] = [min(Y[i] + [INF]), max(Y[i] + [-INF])]


def calc_area(t):
    if t < 0:
        return INF

    x_l, x_r = INF, -INF
    x_l, x_r = min(x_l, X[0][0] + i * t), max(x_r, X[0][1] + i * t)
    x_l, x_r = min(x_l, X[1][0] - i * t), max(x_r, X[1][1] - i * t)
    x_l, x_r = min(x_l, X[2][0]), max(x_r, X[2][1])

    y_l, y_r = INF, -INF
    y_l, y_r = min(y_l, Y[0][0] + i * t), max(y_r, Y[0][1] + i * t)
    y_l, y_r = min(y_l, Y[1][0] - i * t), max(y_r, Y[1][1] - i * t)
    y_l, y_r = min(y_l, Y[2][0]), max(y_r, Y[2][1])

    return (x_r - x_l) * (y_r - y_l)


opt = fmin(calc_area, x0=10**8, ftol=10**(-10), disp=False)
print(calc_area(opt[0]))
