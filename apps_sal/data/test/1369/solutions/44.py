N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]


def dist(x, y, u, v):
    return ((x - u)**2 + (y - v)**2)**0.5


def mxR(x, y):
    return max([dist(x, y, u, v) for u, v in XY])


ans = 10**18
for i, A in enumerate(XY):
    ans = min(ans, mxR(A[0], A[1]))
    for j, B in enumerate(XY[i + 1:]):
        ans = min(ans, mxR((A[0] + B[0]) / 2, (A[1] + B[1]) / 2))

        for C in XY[j + 1:]:
            Z = [0, 0]

            a, b, c = dist(*(B + C)), dist(*(C + A)), dist(*(A + B))

            S = a**2 * (b**2 + c**2 - a**2) + b**2 * (c**2 + a**2 - b**2) + c**2 * (a**2 + b**2 - c**2)
            if S == 0:
                continue

            x = (a**2 * (b**2 + c**2 - a**2) * A[0] + b**2 * (c**2 + a**2 - b**2) * B[0] + c**2 * (a**2 + b**2 - c**2) * C[0]) / S
            y = (a**2 * (b**2 + c**2 - a**2) * A[1] + b**2 * (c**2 + a**2 - b**2) * B[1] + c**2 * (a**2 + b**2 - c**2) * C[1]) / S

            ans = min(ans, mxR(x, y))

print(ans)
