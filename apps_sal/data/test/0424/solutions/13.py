def max_less_prime_divisor(n):  # 1 for primes
    d, max_d = 2, 1
    while d * d <= n:
        while n % d == 0:
            max_d = d
            n //= d
        d += 1
    return n if n != 1 and max_d != 1 else max_d


n = int(input())
m = n - max_less_prime_divisor(n) + 1
answer = m
is_prime = [True] * m
for i in range(2, m):
    if is_prime[i]:
        d = (m - 1) - (m - 1) % i
        if d + i <= n:
            answer = min(answer, d + 1)
        for j in range(i * i, m, i):
            is_prime[j] = False
print(answer)
