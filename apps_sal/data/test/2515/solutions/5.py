from itertools import accumulate
n = 10**5 + 1
primes = set(range(3, n+1, 2))

for i in range(3, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes.add(2)


def like_2017(n):
    return n in primes and (n + 1) // 2 in primes


result = [0] * 10**5
for i in range(1, 10**5 + 1, 2):
    result[i] = like_2017(i)


cumsum = list(accumulate(result))

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l - 1])
