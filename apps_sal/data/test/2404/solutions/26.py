def prime_factor(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n != 1:
        factors.append(n)
    return factors

a = int(input())
print(''.join(map(str, prime_factor(a))))
