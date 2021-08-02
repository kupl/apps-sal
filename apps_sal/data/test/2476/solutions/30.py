import itertools
import collections
N = int(input())
A = [int(_) for _ in input().split()]
c = sorted(collections.Counter(A).values())
acc = list(itertools.accumulate([0] + c))
n = len(acc) - 1
j = 0
for i in range(1, n + 1):
    r = 0
    while i - j > 0:
        if (i - j) * c[-1 - j] <= acc[-1 - j]:
            r = acc[-1 - j] // (i - j)
            break
        else:
            j += 1
    print(r)
for _ in range(N - n):
    print((0))
