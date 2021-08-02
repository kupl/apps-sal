import numpy as np


def divisor(x):
    div = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            div.append(i)
            if x != i**2: div.append(x // i)
    return div


def mincount(a, x):

    minus = np.sort(a % x)
    adj_sum = minus.sum()
    convert = adj_sum // x

    return adj_sum - minus[-convert:].sum()


N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))

div = divisor(A.sum())
div.sort(reverse=True)

for d in div:
    if mincount(A, d) <= K:
        print(d)
        break
