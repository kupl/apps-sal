#  愚直に数え上げる方法

import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():

    N = list(map(int, input()))
    K = int(input())

    if K == 1:
        ans = (len(N) - 1) * 9 + N[0]

    elif K == 2:

        if len(N) < 2:
            print((0))
            return

        ans = (9 ** 2) * (len(N) - 1) * (len(N) - 2) // 2
        ans += (N[0] - 1) * (len(N) - 1) * 9

        for i in range(1, len(N)):
            if N[i] != 0:
                ans += N[i] + (len(N) - i - 1) * 9
                break

    elif K == 3:

        if len(N) < 3:
            print((0))
            return

        ans = (9 ** 3) * (len(N) - 1) * (len(N) - 2) * (len(N) - 3) // 6
        ans += (N[0] - 1) * (9 ** 2) * (len(N) - 1) * (len(N) - 2) // 2

        for i in range(1, len(N) - 1):
            if N[i] != 0:
                ans += (9 ** 2) * (len(N) - i - 1) * (len(N) - i - 2) // 2
                ans += (N[i] - 1) * (len(N) - i - 1) * 9
                for j in range(i + 1, len(N)):
                    if N[j] != 0:
                        ans += N[j] + (len(N) - j - 1) * 9
                        break
                break

    print(ans)


def __starting_point():
    solve()


__starting_point()
