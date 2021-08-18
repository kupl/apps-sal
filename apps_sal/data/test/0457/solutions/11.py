import math

X, N = map(int, input().split())


def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor


def power_func(a, n, p):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


def main():
    NUM = {}
    for num in prime(X).keys():
        a = N
        c = 0
        while a > 0:
            a //= num
            c += a
        NUM[num] = c

    mod = int(1E9 + 7)
    ans = 1
    for num, c in NUM.items():
        ans = (ans * power_func(num, c, mod)) % mod

    print(ans)


def __starting_point():
    main()


__starting_point()
