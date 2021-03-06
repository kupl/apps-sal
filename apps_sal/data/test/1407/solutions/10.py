import sys
import threading
import os.path
import collections
import heapq
import math
import bisect
import string
from platform import python_version
import itertools
sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 27)


def generate_primes(n):
    res = []
    isPrime = [True] * (n * 5)
    (isPrime[0], isPrime[1]) = (0, 0)
    '\n    for (ll i = 2; i*i <= n+1; ++i) {\n        if (isPrime[i]) {\n            for (ll j = i * 2; j <= n; j += i)\n                isPrime[j] = 0;\n        }\n    }\n    '
    for i in range(2, n + 1):
        if i * i > n + 1:
            break
        if isPrime[i]:
            for j in range(i * 2, n + 1, i):
                isPrime[j] = 0
    res.append(2)
    for i in range(3, n + 1, 2):
        if isPrime[i]:
            res.append(i)
    return res


def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    (n, m) = list(map(int, input.readline().split()))
    mat = []
    for i in range(n):
        mat.append(list(map(int, input.readline().split())))
    allprimes = generate_primes(150000)
    tostore = []
    for i in range(n):
        tostore.append([])
        for j in range(m):
            x = bisect.bisect(allprimes, mat[i][j])
            if allprimes[x - 1] == mat[i][j]:
                tostore[i].append(0)
            else:
                tostore[i].append(abs(mat[i][j] - allprimes[x]))
    '\n    for i in range(n):\n        for j in range(m):\n            print(tostore[i][j], end=" ")\n        print()\n    '
    (rowsum, colsum) = ([0] * 501, [0] * 501)
    for i in range(n):
        for j in range(m):
            rowsum[i] += tostore[i][j]
            colsum[j] += tostore[i][j]
    minone = min(min(rowsum[:n]), min(colsum[:m]))
    output = minone
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


def __starting_point():
    main()


__starting_point()
