import math
from functools import reduce

n = int(input())
a = list(map(int, input().split()))


def eratosthenes(limit):
    A = [i for i in range(2, limit + 1)]
    P = []

    while True:
        prime = min(A)

        if prime > math.sqrt(limit):
            break

        P.append(prime)

        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1

    for a in A:
        P.append(a)

    return P


def factorization(n, D):
    arr = []
    temp = n
    for i in D:
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def decomp(n, D):
    arr = []
    while n != 1:
        if D[n] not in arr:
            arr.append(D[n])
        n = n // D[n]
    return arr


D = [i for i in range(10**6 + 1)]

for i in range(2, 10**3 + 1):
    if D[i] == i:
        for n in range(i, 10**6 + 1, i):
            if D[n] == n:
                D[n] = i

s = set()
for i in a:
    for j in decomp(i, D):
        if j not in s:
            s.add(j)
        else:
            if gcd_list(a) == 1:
                print('setwise coprime')
                return
            else:
                print('not coprime')
                return

print('pairwise coprime')
