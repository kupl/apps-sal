from bisect import bisect_left
from itertools import accumulate

n, q = input().split()

n = int(n)
q = int(q)

a = list(map(int, input().split()))
k = list(map(int, input().split()))

reqArrows = sum(a)
prevArrows = 0
accuA = list(accumulate(a))
accuK = list(accumulate(k))

for i in range(q):
    prevArrows += k[i]
    if prevArrows >= reqArrows:
        print(n)
        prevArrows = 0
    else:
        x = bisect_left(accuA, prevArrows)
        if accuA[x] == prevArrows:
            print(n - x - 1)
        else:
            print(n - x)
