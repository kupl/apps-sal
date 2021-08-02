import math


def main():
    n, d = list(map(int, input().split()))
    Xs = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i, xi in enumerate(Xs):
        for xj in Xs[i + 1:]:
            dis = 0
            for di in range(d):
                dis += (xi[di] - xj[di])**2

            if math.sqrt(dis) % 1 == 0:
                ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
