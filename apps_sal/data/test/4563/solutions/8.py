import sys


def v():
    N = int(sys.stdin.readline())
    P = []
    pt, pa = tuple(map(int, sys.stdin.readline().split()))
    res = pt + pa
    for _ in [0] * (N - 1):
        xt, xa = tuple(map(int, sys.stdin.readline().split()))
        xs = xt + xa
        kt = pt // xt if pt % xt == 0 else pt // xt + 1
        ka = pa // xa if pa % xa == 0 else pa // xa + 1
        k = max([kt, ka])
        pt, pa = k * xt, k * xa
        res = pt + pa
    print(res)


def __starting_point(): v()


__starting_point()
