from collections import Counter


def factors(n):
    fact = Counter()
    i = 2
    while i * i <= n:
        while n % i == 0:
            fact[i] += 1
            n //= i
        i += 1
    if n != 1:
        fact[n] += 1
    fact[1] = 1
    return fact


def solve(a, b, c):
    fact = {i: factors(i) for i in range(1, max(a, b, c) + 1)}
    ans = 0
    cache = {}
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                p = i * j * k
                if p not in cache:
                    f = fact[i] + fact[j] + fact[k]
                    f[1] = 1
                    res = 1
                    for (k, v) in list(f.items()):
                        res *= v + 1
                    cache[p] = res // 2
                ans += cache[p]
    return ans % 1073741824


def main():
    (a, b, c) = list(map(int, input().split()))
    ans = solve(a, b, c)
    print(ans)


def __starting_point():
    main()


__starting_point()
