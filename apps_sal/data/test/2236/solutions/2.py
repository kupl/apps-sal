from collections import Counter
from itertools import accumulate
n = int(input())
A = (int(x) for x in input().split())
print(n-max(Counter(accumulate(A)).values()))

