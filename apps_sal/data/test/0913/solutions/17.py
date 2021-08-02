import sys


def solve(N, R, B):
    less = 0
    eq = 0
    more = 0
    for i in range(N):
        if R[i] < B[i]:
            less += 1
        elif R[i] > B[i]:
            more += 1
        else:
            eq += 1
    if more == 0:
        return -1
    d, r = divmod(less, more)
    if r == 0:
        return d + 1
    return d + 1


def __starting_point():
    N, = list(map(int, input().split()))
    R = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = solve(N, R, B)
    print(ans)


__starting_point()
