N = int(input())
(*A,) = list(map(int, input().split()))
mod = 10 ** 9 + 7
MAX = 1000000


def gen_primes(n):
    n = int(n ** 0.5) + 2
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if is_prime[i]:
            for j in range(2 * i, n, i):
                is_prime[j] = False
    return [i for (i, flag) in enumerate(is_prime) if flag]


C = [0] * (MAX + 1)
primes = gen_primes(MAX)


def prime_fact(n):
    cnt = 0
    for p in primes:
        if n % p:
            continue
        while n % p == 0:
            cnt += 1
            n //= p
        C[p] = max(C[p], cnt)
        cnt = 0
    if n != 1:
        C[n] = 1


for a in A:
    prime_fact(a)
lcm = 1
for (i, c) in enumerate(C):
    if c:
        lcm = lcm * pow(i, c, mod) % mod
ans = 0
for a in A:
    ans = (ans + lcm * pow(a, mod - 2, mod) % mod) % mod
print(ans)
