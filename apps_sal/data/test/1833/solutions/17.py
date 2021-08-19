MOD = int(1000000000.0 + 7)
N = int(input())
A = list(map(int, input().split()))
ways = [0] * (N + 1)
ways[0] = 1
for a in A:
    factors = []
    big_factors = []
    x = 1
    while x * x <= a:
        if a % x == 0:
            factors.append(x)
            if x * x < a:
                big_factors.append(a // x)
        x += 1
    factors.reverse()
    for x in big_factors:
        if x <= N:
            ways[x] += ways[x - 1]
            if ways[x] >= MOD:
                ways[x] -= MOD
    for x in factors:
        if x <= N:
            ways[x] += ways[x - 1]
            if ways[x] >= MOD:
                ways[x] -= MOD
print((sum(ways) - 1) % MOD)
