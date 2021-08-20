import collections
import math
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
primes_arr = [-1]
maxi = 2750131 + 1
primes_sieve = [0 for _ in range(maxi)]


def sieve():
    for i in range(2, maxi):
        if not primes_sieve[i]:
            primes_arr.append(i)
            primes_sieve[i] = 1
            for j in range(i * i, maxi, i):
                if not primes_sieve[j]:
                    primes_sieve[j] = i


sieve()
d = collections.defaultdict(int)
z = collections.defaultdict(int)
ans = []
primes = []
for i in range(n * 2):
    x = a[i] // primes_sieve[a[i]]
    if d[a[i]] > 0:
        d[a[i]] -= 1
    elif x != a[i]:
        d[x] += 1
        ans.append(a[i])
    else:
        primes.append(a[i])
primes = primes[::-1]
for i in range(len(primes)):
    if z[primes[i]] > 0:
        z[primes[i]] -= 1
    else:
        z[primes_arr[primes[i]]] += 1
        ans.append(primes[i])
print(*ans)
