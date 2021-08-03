from math import pi, sin, cos

T = int(input().strip())
for t in range(T):
    n = int(input().strip())
    alpha = pi / n
    R = 1 / (2 * sin(alpha / 2))
    if n % 2 == 0:
        gamma = alpha / 2
    else:
        k = n // 2
        gamma = (pi / 2 - alpha * k) / 2

    # print(alpha*180/pi)
    # print(gamma * 180 / pi)
    res = R * 2 * cos(gamma)
    print(res)
