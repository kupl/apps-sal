def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def d(x):
    y = 0
    ans = 1
    for i in primes_list:
        if x < i:
            break
        y = 1
        while x % i == 0 and x >= i:
            x /= i
            y += 1
        ans *= y
    return ans


primes_list = primes1(100)
x = 0
t = {}
(a, b, c) = list(map(int, input().split()))
s = []
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            q = i * j * k
            if q not in t:
                t[q] = d(q)
            x += t[q]
print(x % 1073741824)
