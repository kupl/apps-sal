(xp, yp, vx, vy, a, b, c, d) = [int(x) for x in input().split()]
L = (vx ** 2 + vy ** 2) ** 0.5
(vx, vy) = (vx / L, vy / L)
A = [0 for i in range(7)]
A[0] = (b * vx, b * vy)
A[1] = (-a * vy / 2, a * vx / 2)
A[2] = (-c * vy / 2, c * vx / 2)
A[3] = (-c * vy / 2 - d * vx, c * vx / 2 - d * vy)
A[4] = (c * vy / 2 - d * vx, -c * vx / 2 - d * vy)
A[5] = (c * vy / 2, -c * vx / 2)
A[6] = (a * vy / 2, -a * vx / 2)
for (x, y) in A:
    print(x + xp, y + yp)
