from collections import defaultdict
mod = 10 ** 9 + 7
INF = float('inf')


def getlist():
    return list(map(int, input().split()))


def inverse(N, mod):
    return pow(N, mod - 2, mod)


def main():
    T = int(input())
    for _ in range(T):
        (x, y) = getlist()
        C = getlist()
        D = [INF] * 8
        D[0] = min(C[5], C[0] + C[4])
        D[1] = min(C[0], C[1] + C[5])
        D[2] = min(C[1], C[0] + C[2])
        D[3] = min(C[1] + C[2], C[0] + 2 * C[2], C[3] + 2 * C[1])
        D[4] = min(C[2], C[1] + C[3])
        D[5] = min(C[3], C[2] + C[4])
        D[6] = min(C[4], C[3] + C[5])
        D[7] = min(C[4] + C[5], C[3] + 2 * C[5], C[0] + 2 * C[4])
        if x >= 0 and y >= 0:
            m = min(x, y)
            ans = D[1] * m + D[0] * (x - m) + D[2] * (y - m)
        elif x >= 0 and y < 0:
            m = min(x, -y)
            ans = D[7] * m + D[0] * (x - m) + D[6] * (-y - m)
        elif x < 0 and y >= 0:
            m = min(-x, y)
            ans = D[3] * m + D[4] * (-x - m) + D[2] * (y - m)
        else:
            m = min(-x, -y)
            ans = D[5] * m + D[4] * (-x - m) + D[6] * (-y - m)
        print(ans)


def __starting_point():
    main()


__starting_point()
