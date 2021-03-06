from collections import Counter
from bisect import bisect_left
from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
a = list(Counter(A).values())
a.sort()
b = list(accumulate(a))
length = len(a)
for i in range(1, N + 1):
    if i == 1:
        print(b[-1])
    elif len(a) < i:
        print(0)
    else:
        n = b[-1] // i
        for j in reversed(range(1, n + 1)):
            t = bisect_left(a, j)
            if j * i <= b[t - 1] + (length - t) * j:
                print(j)
                break
