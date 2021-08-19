def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = set()
for i in range(2, 100000):
    if isPrime(i):
        primes.add(i)
c = [1] + [0] * 100000
n = input()
s = list(map(int, input().split()))
x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
for i in s:
    for p in x:
        if i in primes:
            c[i] += 1
            break
        if p ** 2 > i:
            break
        if i % p == 0:
            c[p] += 1
            while i and i % p == 0:
                i //= p
m = max(c)
print(m)
