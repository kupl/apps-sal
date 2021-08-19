import math


def solve(N):
    if N == 0:
        print('0')
        return
    ans = ''
    while N != 0:
        m = N % 2
        ans = str(m) + ans
        N = (N - m) * -1 >> 1
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)


__starting_point()
