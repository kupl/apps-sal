from collections import Counter


def mod_pow(a, n, mod):
    """
    二分累乗法による a^n (mod m)の実装
    :param a: 累乗の底
    :param n: 累乗の指数
    :param mod: 法
    :return: a^n (mod m)
    """

    result = 1
    a_n = a
    while n > 0:
        if n & 1:
            result = result * a_n % mod
        a_n = a_n * a_n % mod
        n >>= 1
    return result


N = int(input())
A = Counter(tuple(map(int, input().split(' '))))
MOD = 10 ** 9 + 7

if A[0] > 1:
    print((0))
elif sum([key for key, value in list(A.items()) if value == 1]) != 0:
    print((0))
else:
    print((mod_pow(2, N // 2, MOD)))
