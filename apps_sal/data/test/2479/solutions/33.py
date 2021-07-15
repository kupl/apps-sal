import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    res = (n - 2) * (n - 2)
    Y = n - 1
    T = n - 1
    yoko = [n - 1] * (n - 1)
    tate = [n - 1] * (n - 1)
    for num, x in query:
        x -= 1
        if num == 1:
            if x > Y:
                res -= tate[x] - 1
            else:
                res -= T - 1
                for i in range(x, Y):
                    tate[i] = T
                Y = x
            tate[x] = 0
        else:
            if x > T:
                res -= yoko[x] - 1
            else:
                res -= Y - 1
                for i in range(x, T):
                    yoko[i] = Y
                T = x
            yoko[x] = 0
    print(res)


def __starting_point():
    resolve()

__starting_point()
