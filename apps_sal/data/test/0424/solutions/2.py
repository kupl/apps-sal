x2 = int(input())

n = 1000001
max_prime_div = [0] * n
sieve = list(range(n))
sieve[1] = 0
for i in sieve:
    if sieve[i]:
        for j in range(2 * i, n, i):
            sieve[j] = 0
            max_prime_div[j] = i

min_x0 = n
for x in range(x2 - max_prime_div[x2] + 1, x2 + 1):
    max_div = max_prime_div[x]
    tmp = x - max_div + 1
    if max_div and tmp < min_x0:
        min_x0 = tmp
    if max_div and x // max_div == 2:
        break
print(min_x0)
