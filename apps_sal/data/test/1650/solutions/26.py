from sys import stdin


def main():
    readline = stdin.readline
    L = readline().strip()
    n = len(L)
    mod = 10 ** 9 + 7
    dpF = [0] * (n + 1)
    dpF[0] = 1
    dpT = [0] * (n + 1)
    for i in range(1, n + 1):
        if L[i - 1] == '1':
            dpF[i] += 2 * dpF[i - 1]
            dpT[i] += dpF[i - 1]
            dpT[i] += 3 * dpT[i - 1]
        else:
            dpF[i] += dpF[i - 1]
            dpT[i] += 3 * dpT[i - 1]
        dpF[i] %= mod
        dpT[i] %= mod
    print((dpF[n] + dpT[n]) % mod)


def __starting_point():
    main()


__starting_point()
