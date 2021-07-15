import sys

input = sys.stdin.readline


def main():
    N, A, B = [int(x) for x in input().split()]
    H = [int(input()) for _ in range(N)]

    def isOK(mid):
        cnt = 0
        for h in H:
            if h > B * mid:
                sabun = h - B * mid
                cnt += 0 - - sabun // (A - B)
                if cnt > mid:
                    return False
        return True

    ok = 10 ** 9
    ng = 0

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


def __starting_point():
    main()

__starting_point()
