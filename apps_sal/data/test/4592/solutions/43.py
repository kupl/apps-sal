N = int(input())

mod = 10 ** 9 + 7


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


L = primes(N)

ans = [0] * (N + 1)
for i in range(2, N + 1):
    for j in L:
        if i < j:
            break
        while True:
            if i % j == 0:
                i //= j
                ans[j] += 1
            else:
                break

ans_num = 1
for i in range(2, N + 1):
    if ans[i] >= 1:
        ans_num *= ans[i] + 1 % mod
print((ans_num % mod))

