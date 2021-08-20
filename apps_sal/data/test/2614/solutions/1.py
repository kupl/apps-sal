from collections import Counter
import math
testCases = int(input())
for _ in range(testCases):
    n = int(input())
    ar = list(map(int, input().split()))
    cntr = dict(Counter(ar))
    cntr = Counter(cntr.values())
    mn = float('inf')
    for x in cntr:
        if x != 1:
            mn = min(mn, int(math.floor((n - cntr[x]) / (x - 1))) - 1)
    print(mn)
