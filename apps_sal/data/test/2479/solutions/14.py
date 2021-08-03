import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    res = (n - 2) * (n - 2)
    R = C = n - 1
    yoko = [n - 1] * (n - 1)
    tate = [n - 1] * (n - 1)
    for x, y in query:
        y -= 1
        if x == 1:
            if y > C:
                res -= tate[y] - 1
            else:
                res -= R - 1
                for c in range(C - 1, y, -1):
                    tate[c] = R
                C = y
            tate[y] = 0
        else:
            if y > R:
                res -= yoko[y] - 1
            else:
                res -= C - 1
                for r in range(R - 1, y, -1):
                    yoko[r] = C
                R = y
            yoko[y] = 0
    print(res)


def __starting_point():
    resolve()


__starting_point()
