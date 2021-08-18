
from math import ceil


def resolve():
    def chick(k):
        cnt = 0
        for i in range(N):
            h = ceil((H[i] - B * k) / (A - B))
            cnt += max(0, h)
        return cnt <= k

    N, A, B = list(map(int, input().split()))
    H = [int(input()) for _ in range(N)]

    ok = 10 ** 10
    ng = 0
    while ok - ng > 1:
        k = (ok + ng) // 2
        if chick(k):
            ok = k
        else:
            ng = k

    print(ok)


def __starting_point():
    resolve()


__starting_point()
