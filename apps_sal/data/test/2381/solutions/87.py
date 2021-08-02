# -*- coding: utf-8 -*-
import sys


def main():
    N, K = list(map(int, sys.stdin.readline().split()))
    A_list = list(map(int, sys.stdin.readline().split()))

    A_list.sort(key=lambda x: -abs(x))
    A_plus = []
    A_minus = []
    mod = 10**9 + 7

    for val in A_list:
        if val >= 0:
            A_plus.append(val)
        else:
            A_minus.append(val)

    ans = 1
    cnt = 0
    i_p = 0  # index of A_plus
    i_m = 0  # index of A_minus

    while (cnt < K):
        if (K - cnt) == 1:
            if i_p < len(A_plus):
                ans *= A_plus[i_p]
                ans %= mod
                cnt += 1
                i_p += 1
                break

            else:
                ans2 = 1

                for i in range(len(A_list) - K, len(A_list)):
                    ans2 *= A_list[i]
                    ans2 %= mod

                print(ans2)
                return

        if (i_m + 1) < len(A_minus):
            if (i_p + 1) < len(A_plus):
                if abs(A_plus[i_p] * A_plus[i_p + 1]) > abs(A_minus[i_m] * A_minus[i_m + 1]):
                    ans *= A_plus[i_p]
                    cnt += 1
                    i_p += 1
                else:
                    ans *= (A_minus[i_m] * A_minus[i_m + 1])
                    cnt += 2
                    i_m += 2

            else:
                ans *= (A_minus[i_m] * A_minus[i_m + 1])
                cnt += 2
                i_m += 2

        else:
            ans *= A_plus[i_p]
            cnt += 1
            i_p += 1

        ans %= mod

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
