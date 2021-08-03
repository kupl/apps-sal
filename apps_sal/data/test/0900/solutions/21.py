import numpy as np


def main():
    n = 13
    mod = 1000000007
    r = 5
    in_str = input()

    amari_l = amari_list(n)
    amari_m = amari_matrix(n, amari_l)

    ans_list = initial(in_str[-1:], n)

    for i, s in enumerate(reversed(in_str)):
        if i == 0:
            continue
        if s == "?":
            ans_list = np.dot(ans_list, amari_m[i % len(amari_m)]) % mod
        else:
            t = int(s) * amari_l[i % len(amari_l)] % n
            ans_list = np.roll(ans_list, t)

    print((int(ans_list[r] % mod)))


def initial(s, n):
    if s == "?":
        return np.array([1 if i < 10 else 0 for i in range(n)], dtype='int64')
    else:
        return np.array([1 if i == int(s) else 0 for i in range(n)], dtype='int64')


def shift(n, r):
    return np.array([[1 if (i - j + r) % n == 0 else 0 for j in range(n)] for i in range(n)])


def amari_list(n):
    ret = []
    for i in range(n + 1):
        r = 10**i % n
        if r in ret:
            return ret
        else:
            ret.append(r)


def amari_matrix(n, amari_list):
    ret = np.zeros((len(amari_list), n, n))
    for i, j in enumerate(amari_list):
        tmp = np.zeros((n, n))
        for k in range(10):
            tmp += shift(n, j * k % n)
        ret[i] = tmp
    return ret


def __starting_point():
    main()


__starting_point()
