import math


def check(k, A, B, H):
    return sum([max([0, math.ceil((h - B * k) / (A - B))]) for h in H]) <= k


def main():
    N, A, B = list(map(int, input().split(' ')))
    H = [int(input()) for _ in range(N)]
    ng, ok = 0, 10**9
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid, A, B, H):
            ok = mid
        else:
            ng = mid
    print(ok)


def __starting_point():
    main()
__starting_point()
