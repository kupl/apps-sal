from collections import Counter
import itertools as ittls
3


def sqr(x):
    return x * x


def inputarray(func=int):
    return list(map(func, input().split()))


N = int(input())
A = list(inputarray())

maxv = 1
currmaxv = 1
for i in range(1, len(A)):
    if A[i] >= A[i - 1]:
        currmaxv = currmaxv + 1
    else:
        currmaxv = 1
    maxv = max(maxv, currmaxv)

print(maxv)
