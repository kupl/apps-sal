from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


def want(n):
    xmax = float('-inf')
    xmin = float('inf')
    ymax = float('-inf')
    ymin = float('inf')
    if L:
        xmax = max(xmax, L_R - n)
        xmin = min(xmin, L_L - n)
        ymax = max(ymax, LR_U)
        ymin = min(ymin, LR_D)
    if R:
        xmax = max(xmax, R_R + n)
        xmin = min(xmin, R_L + n)
        ymax = max(ymax, LR_U)
        ymin = min(ymin, LR_D)
    if D:
        xmax = max(xmax, UD_R)
        xmin = min(xmin, UD_L)
        ymax = max(ymax, D_U - n)
        ymin = min(ymin, D_D - n)
    if U:
        xmax = max(xmax, UD_R)
        xmin = min(xmin, UD_L)
        ymax = max(ymax, U_U + n)
        ymin = min(ymin, U_D + n)
    return abs(xmax - xmin) * abs(ymax - ymin)


def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


N = int(input())
UD_L = float('inf')
UD_R = float('-inf')
L_L = float('inf')
L_R = float('-inf')
R_L = float('inf')
R_R = float('-inf')
LR_D = float('inf')
LR_U = float('-inf')
D_D = float('inf')
D_U = float('-inf')
U_D = float('inf')
U_U = float('-inf')
U = False
D = False
L = False
R = False
for i in range(N):
    (x, y, d) = input().split()
    x = int(x)
    y = int(y)
    if d == 'L' or d == 'R':
        LR_D = min(LR_D, y)
        LR_U = max(LR_U, y)
        if d == 'L':
            L_L = min(L_L, x)
            L_R = max(L_R, x)
            L = True
        else:
            R_L = min(R_L, x)
            R_R = max(R_R, x)
            R = True
    if d == 'D' or d == 'U':
        UD_L = min(UD_L, x)
        UD_R = max(UD_R, x)
        if d == 'D':
            D_D = min(D_D, y)
            D_U = max(D_U, y)
            D = True
        else:
            U_D = min(U_D, y)
            U_U = max(U_U, y)
            U = True
t0 = 0
t3 = 2 * 10 ** 8
last = float('inf')
ans = 1000000000000000000000
while abs(last - ans) > 10 ** (-100):
    t1 = Decimal(t0 * 2 + t3 * 1) / Decimal(3)
    t2 = Decimal(t0 * 1 + t3 * 2) / Decimal(3)
    last = ans
    if want(t1) <= want(t2):
        ans = want(t1)
        t3 = t2
    else:
        ans = want(t2)
        t0 = t1
if ans <= 10 ** (-9):
    ans = 0
print('{:.20g}'.format(ans))
