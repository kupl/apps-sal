from collections import defaultdict


def decompose(n):
    x = n
    i = 2
    fac = defaultdict(lambda: 0)
    while i * i <= n:
        while x % i == 0:
            fac[i] += 1
            x = x // i
        if x == 1:
            break
        i += 1
    if x != 1:
        fac[x] += 1
    return fac


def main():
    n, b = list(map(int, input().split()))
    require = decompose(b)
    ans = 10**18
    for key, val in list(require.items()):
        n2 = n
        acc = 0
        while n2 > 0:
            acc += n2 // key
            n2 //= key
        ans = min(ans, acc // val)
    print(ans)


def __starting_point():
    main()


__starting_point()
