from functools import reduce


def main():
    from itertools import product
    from functools import reduce
    from operator import mul
    a, b, c = sorted(map(int, input().split()))
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    l = [None]
    for x in range(1, (c + 1)):
        tmp = [0] * 25
        for i, p in enumerate(primes):
            while not x % p:
                x //= p
                tmp[i] += 1
        l.append(tuple(tmp))
    res = 0
    cache = {}
    for x, y, z in product(list(range(1, a + 1)), list(range(1, b + 1)), list(range(1, c + 1))):
        xyz = x * y * z
        if xyz in cache:
            res += cache[xyz]
        else:
            cache[xyz] = u = (
                reduce(mul, list(map(sum, list(zip(
                    l[x], l[y], l[z], (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))))),
                    1) & 1073741823)
            res += u
    print(res & 1073741823)


def __starting_point():
    main()


__starting_point()
