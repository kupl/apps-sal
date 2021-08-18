from math import floor, sqrt


def siv(limit, primes):
    mark = [False] * (limit + 1)
    for i in range(2, limit + 1):
        if not mark[i]:
            primes.append(i)
            for j in range(i, limit + 1, i):
                mark[j] = True


def pir(low, high, prims):
    limit = floor(sqrt(high)) + 1
    primes = list()
    siv(limit, primes)
    n = high - low + 1
    mark = [False] * (n + 1)
    for i in range(len(primes)):
        loLim = floor(low / primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]
        for j in range(loLim, high + 1, primes[i]):
            mark[j - low] = True
    pc = 0
    for i in range(low, high + 1):
        if not mark[i - low]:
            prims.append(i)
            pc += 1
    return pc


a, b, k = [int(i) for i in input().split()]

prims = []
pc = pir(a, b, prims)
if pc != 0 and prims[0] == 1:
    prims.remove(1)
    pc -= 1

if pc < k:
    print(-1)
    return

mx = max(prims[k - 1] - a + 1, b - prims[len(prims) - k] + 1)

for i in range(len(prims) - k):
    mx = max(prims[i + k] - prims[i], mx)

print(mx)
