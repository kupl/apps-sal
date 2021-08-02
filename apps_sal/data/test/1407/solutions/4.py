def is_prime(x, primes):
    for i in primes:
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


n, m = [int(x) for x in input().split()]
a = []
primes = []
for i in range(2, 110000):
    if is_prime(i, primes):
        primes.append(i)
next = [0] * 110000
next[0] = 2
for x in primes:
    val = x
    while next[x] == 0:
        next[x] = val
        x -= 1
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        a[i][j] = next[a[i][j]] - a[i][j]
print(min(min(sum(x) for x in a), min(sum(x) for x in zip(*a))))
