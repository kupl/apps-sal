import sys
input = sys.stdin.readline
Q = int(input())
primes = set()
not_p = set()
for i in range(2, 10 ** 5 + 1):
    if i not in not_p:
        primes.add(i)
        for j in range(i + i, 10 ** 5 + 1, i):
            not_p.add(j)
acum = [0 for _ in range(10 ** 5 + 1)]
for i in range(3, 10 ** 5 + 1, 2):
    if i in primes and (i + 1) // 2 in primes:
        acum[i] += 1
    acum[i] += acum[i - 2]
for _ in range(Q):
    (l, r) = map(int, input().split())
    print(acum[r] - acum[l - 2])
