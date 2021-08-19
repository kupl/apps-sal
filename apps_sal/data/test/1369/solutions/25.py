from scipy.optimize import fmin
I = input
n = int(I())
L = [list(map(int, I().split())) for i in range(n)]


def C(t):
    (i, j) = t
    return max(((x - i) ** 2 + (y - j) ** 2 for (x, y) in L))


(x, y) = fmin(C, (500, 500), disp=0)
print(C((x, y)) ** 0.5)
