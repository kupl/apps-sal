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

    select = []
    i_p = 0
    i_m = 0

    while (len(select) < K):
        if (K - len(select)) == 1:
            if i_p < len(A_plus):
                select.append(A_plus[i_p])
                i_p += 1
                break

            else:
                ans = 1

                for i in range(len(A_list) - K, len(A_list)):
                    ans *= A_list[i]
                    ans %= mod

                print(ans)
                return

        if (i_m + 1) < len(A_minus):
            if (i_p + 1) < len(A_plus):
                if abs(A_plus[i_p] * A_plus[i_p + 1]) > abs(A_minus[i_m] * A_minus[i_m + 1]):
                    select.append(A_plus[i_p])
                    i_p += 1
                else:
                    select.extend([A_minus[i_m], A_minus[i_m + 1]])
                    i_m += 2

            else:
                select.extend([A_minus[i_m], A_minus[i_m + 1]])
                i_m += 2

        else:
            select.append(A_plus[i_p])
            i_p += 1

    ans = 1

    for i in range(K):
        ans *= select[i]
        ans %= mod

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
