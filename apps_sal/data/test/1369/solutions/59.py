N = int(input())
XY = [complex(*list(map(int, input().split()))) for _ in range(N)]
ans = 10 ** 18


def calc(center):
    return max((abs(center - x) for x in XY))


for A in XY:
    for B in XY:
        center = (A + B) / 2
        ans = min(ans, calc(center))
        for C in XY:
            (a, b, c) = (abs(B - C), abs(C - A), abs(A - B))
            S = 0
            T = complex(0, 0)
            for ((x, y, z), u) in zip([(a, b, c), (b, c, a), (c, b, a)], (A, B, C)):
                O = x ** 2 * (y ** 2 + z ** 2 - x ** 2)
                S += O
                T += O * u
            if S == 0:
                continue
            ans = min(ans, calc(T / S))
print(ans)
