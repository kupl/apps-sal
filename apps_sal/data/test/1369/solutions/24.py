import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    P = [[int(x) for x in input().split()] for _ in range(N)]
    eps = 1e-09
    minR = 10 ** 10
    if N == 2:
        r = (P[1][0] - P[0][0]) ** 2 + (P[1][1] - P[0][1]) ** 2
        r = r ** 0.5 / 2
        print(r)
        return 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            (a, b) = P[i]
            (c, d) = P[j]
            (x, y) = ((a + c) / 2, (b + d) / 2)
            rd = (x - a) ** 2 + (y - b) ** 2
            for l in range(N):
                if l != i and l != j:
                    if (P[l][0] - x) ** 2 + (P[l][1] - y) ** 2 - rd > eps:
                        break
            else:
                minR = min(minR, rd)
            for k in range(j + 1, N):
                if (P[j][1] - P[i][1]) * (P[k][0] - P[j][0]) == (P[j][0] - P[i][0]) * (P[k][1] - P[j][1]):
                    continue
                (e, f) = P[k]
                if c == a:
                    y = (d + b) / 2
                    if d == f:
                        x = (d + f) / 2
                    else:
                        x = (e + c) / 2 + ((d + f) / 2 - y) * (f - d) / (e - c)
                elif e == c:
                    y = (d + f) / 2
                    if d == b:
                        x = (d + b) / 2
                    else:
                        x = (a + c) / 2 + ((b + d) / 2 - y) * (d - b) / (c - a)
                elif d == b:
                    x = (a + c) / 2
                    y = (d + f) / 2 + ((e + c) / 2 - x) * (e - c) / (f - d)
                elif f == d:
                    x = (c + e) / 2
                    y = (b + d) / 2 + ((c + a) / 2 - x) * (c - a) / (d - b)
                else:
                    x = ((c ** 2 - a ** 2) / (2 * (d - b)) - (e ** 2 - c ** 2) / (2 * (f - d)) - (f - b) / 2) * ((d - b) * (f - d) / ((c - a) * (f - d) - (e - c) * (d - b)))
                    y = (d + f) / 2 + ((e + c) / 2 - x) * (e - c) / (f - d)
                rd = (x - a) ** 2 + (y - b) ** 2
                for l in range(N):
                    if l != i and l != j and (l != k):
                        if (P[l][0] - x) ** 2 + (P[l][1] - y) ** 2 - rd > eps:
                            break
                else:
                    minR = min(minR, rd)
    print(minR ** 0.5)
    return 0


def __starting_point():
    solve()


__starting_point()
