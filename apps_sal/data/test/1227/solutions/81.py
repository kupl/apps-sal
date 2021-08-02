import sys

read = sys.stdin.read


def main():
    N, K = list(map(int, read().split()))

    dp1 = [0] * (K + 1)
    dp2 = [0] * (K + 1)
    dp1[0] = 1

    for x in map(int, str(N)):
        for j in range(K, -1, -1):
            if j > 0:
                dp2[j] += dp2[j - 1] * 9
                if x != 0:
                    dp2[j] += dp1[j - 1] * (x - 1) + dp1[j]
                    dp1[j] = dp1[j - 1]
            else:
                dp1[j] = 0
                dp2[j] = 1

    print((dp1[K] + dp2[K]))
    return


def __starting_point():
    main()


__starting_point()
