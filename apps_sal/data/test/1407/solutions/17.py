from bisect import bisect_left as bl
p = 10**5 + 10


def sieve():
    l = [True] * p
    i = 2
    while i * i <= p:
        if l[i]:
            for j in range(i * i, p, i):
                l[j] = False
        i += 1
    primes = []
    for i in range(2, p):
        if l[i]:
            primes.append(i)
    return primes


primes = sieve()
n, m = list(map(int, input().split()))
req = [[0 for i in range(m)]for j in range(n)]

mat = []
for i in range(n):
    mat.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        curr = mat[i][j]
        ind = bl(primes, curr)
        g = primes[ind]
        req[i][j] = g - curr
mini = 1000000000
for i in range(n):
    curr = sum(req[i])
    if curr < mini:
        mini = curr
for j in range(m):
    curr = 0
    for i in range(n):
        curr += req[i][j]
    if curr < mini:
        mini = curr
print(mini)
