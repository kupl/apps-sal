def prin_pram(x, y):
    nonlocal A
    nonlocal B
    nonlocal C
    if A * x + B * y + C == 0:
        return 1
    else:
        return 0


n, x0, y0 = list(map(int, input().split()))
xyi = [list(map(int, input().split())) for i in range(n)]
number = 0
i = 0
A = 0
B = 0
C = 0
z = 0
while number < n:
    i = 0
    A = xyi[0][1] - y0
    B = x0 - xyi[0][0]
    C = x0 * (y0 - xyi[0][1]) + y0 * (xyi[0][0] - x0)
    for j in range(n - number):
        temp = prin_pram(xyi[j][0], xyi[j][1])
        if temp == 1:
            number += 1
        else:
            xyi[i][0] = xyi[j][0]
            xyi[i][1] = xyi[j][1]
            i += 1
    z += 1
print(z)
