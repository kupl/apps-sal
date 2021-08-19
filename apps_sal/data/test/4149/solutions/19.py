import math
import sys
MAXP = 2750131
MAXPN = 199999
isPrime = [True] * (MAXP + 1)
primeDict = {}
countNum = {}
SPF = {}


def initPrime(pC):
    isPrime[0] = isPrime[1] = False
    for i in range(2, MAXP + 1):
        if isPrime[i]:
            primeDict[i] = pC
            pC += 1
            for j in range(i ** 2, MAXP + 1, i):
                isPrime[j] = False
                if j not in SPF:
                    SPF[j] = i


n = int(input())
b = [int(x) for x in input().split()]
b.sort(reverse=True)
initPrime(1)
a = list()
for i in b:
    countNum[i] = countNum.get(i, 0) + 1
for i in b:
    if isPrime[i]:
        if countNum[i] > 0:
            countNum[primeDict[i]] -= 1
            countNum[i] -= 1
            a.append(primeDict[i])
    elif countNum[i] > 0:
        countNum[i / SPF[i]] -= 1
        countNum[i] -= 1
        a.append(i)
for i in a:
    print(i, end=' ')
