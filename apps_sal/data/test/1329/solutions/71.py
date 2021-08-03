from collections import defaultdict


def main():
    n = int(input())
    fact = defaultdict(int)
    for i in range(2, n + 1):
        j = i
        while j % 2 == 0:
            j //= 2
            fact[2] += 1
        k = 3
        while k * k <= j:
            if j % k:
                k += 2
            else:
                j //= k
                fact[k] += 1
        if j != 1:
            fact[j] += 1
    fact = list(fact.items())
    length = len(fact)
    ans = 0
    for i in range(length):
        if fact[i][1] >= 74:
            ans += 1
    product = set()
    for small_p, large_p in [[2, 24], [4, 14]]:
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                now = pow(fact[i][0], large_p) * pow(fact[j][0], small_p)
                if fact[i][1] >= large_p and fact[j][1] >= small_p and now not in product:
                    ans += 1
                    product.add(now)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if i == j or j == k or i == k:
                    continue
                now = pow(fact[i][0], 4) * pow(fact[j][0], 4) * pow(fact[k][0], 2)
                if fact[i][1] >= 4 and fact[j][1] >= 4 and fact[k][1] >= 2 and now not in product:
                    ans += 1
                    product.add(now)
    print(ans)


def __starting_point():
    main()


__starting_point()
