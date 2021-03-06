def make_prime_table(N):
    sieve = list(range(N + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, N + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


N = int(input())
A = list(map(int, input().split()))
m = 1000000007
prime_table = make_prime_table(1000000)
lcm_factors = {}
for i in range(N):
    t = []
    a = A[i]
    while a != 1:
        if len(t) != 0 and t[-1][0] == prime_table[a]:
            t[-1][1] += 1
        else:
            t.append([prime_table[a], 1])
        a //= prime_table[a]
    for (k, v) in t:
        if k not in lcm_factors or lcm_factors[k] < v:
            lcm_factors[k] = v
lcm = 1
for k in lcm_factors:
    for i in range(lcm_factors[k]):
        lcm *= k
        lcm %= m
result = 0
for i in range(N):
    result += lcm * pow(A[i], m - 2, m)
    result %= m
print(result)
