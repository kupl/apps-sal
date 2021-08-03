import numpy as np


def isPrime_np(n):
    maxp = int(np.sqrt(n))
    searchlist = [i for i in range(2, n + 1)]
    primeNum = []

    while searchlist[0] <= maxp:
        primeNum.append(searchlist[0])
        tmp = searchlist[0]
        searchlist = [i for i in searchlist if i % tmp != 0]
    primeNum.extend(searchlist)

    return primeNum


MaxQ = 10**5 + 1
Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]

a = [0] * MaxQ
s = [0] * MaxQ
prime = isPrime_np(MaxQ)
pset = set(prime)
for p in prime:
    if (p + 1) / 2 in pset:
        a[p] = 1

ans = []
s = np.cumsum(a)

for l, r in lr:
    ans.append(s[r] - s[l - 1])
print(*ans, sep="\n")
