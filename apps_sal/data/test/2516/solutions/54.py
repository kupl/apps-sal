from math import factorial
import collections


def permutations_count(n, r):
    ''' 順列 '''
    return factorial(n) // factorial(n - r)


def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))


n, p = map(int, input().split())
S = input()
su = 0

if p > 6 or p == 3:

    lis = []
    amari = 1
    lis.append(int(S[-1]) % p)

    for i in range(2, len(S) + 1):
        amari = (amari * 10) % p
        lis.append((int(S[-1 * i]) * amari + lis[i - 2]) % p)

    c = collections.Counter(lis)

    for k in c:
        if c[k] > 1:
            su += combinations_count(c[k], 2)

    su += c[0]

    print(su)

else:
    S = S[::-1]
    for i in range(len(S)):
        if int(S[i]) % p == 0:
            su += len(S) - i
    print(su)
