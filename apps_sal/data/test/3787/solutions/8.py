def main():
    N, A, B = list(map(int, input().split()))

    if not (((N - 1) // A + 1) <= B <= (N - A) + 1):
        print((-1))
        return

    if B == 1:
        print((*list(range(1, N + 1))))
        return

    q, r = divmod(N - A, B - 1)

    ctr = [A]
    ctr += [q] * (B - 1 - r)
    ctr += [q + 1] * r

    ans = []
    ma = N
    for x in ctr:
        ans += list(range(ma - x + 1, ma + 1))
        ma -= x
    print((*ans))


def __starting_point():
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())


__starting_point()
