a, b, c = [int(x) for x in input().split(' ')]
mod = 1073741824


def divisors(x):
    powers = {}
    i = 2
    while(x != 1):
        if x % i == 0:
            if i in powers:
                powers[i] += 1
            else:
                powers[i] = 1
            x //= i
        else:
            i += 1
    return powers


primeFactors = {}

for x in range(1, 101):
    primeFactors[x] = divisors(x)


def finalMapPrepare(finalMap, x):
    for k in primeFactors[x]:
        if k in finalMap:
            finalMap[k] += primeFactors[x][k]
        else:
            finalMap[k] = primeFactors[x][k]


total = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            finalMap = {}
            finalMapPrepare(finalMap, i)
            finalMapPrepare(finalMap, j)
            finalMapPrepare(finalMap, k)
            ans = 1
            for v in finalMap.values():
                ans *= (v + 1)
            total += (ans) % mod
print(total % mod)
