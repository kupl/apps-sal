from math import gcd, sqrt, ceil, inf, factorial, log2
from bisect import bisect
from collections import defaultdict
from math import gcd, sqrt, ceil, inf
from collections import Counter
import sys
sys.setrecursionlimit(1000000)
t = int(input())
for i in range(t):
    n = int(input())
    l1 = list(map(int, input().split()))
    m = int(input())
    l2 = list(map(int, input().split()))
    count1 = 0
    for i in l2:
        if i % 2 == 0:
            count1 += 1
    count2 = m - count1
    ans = 0
    for i in l1:
        if i % 2 == 0:
            ans += count1
        else:
            ans += count2
    print(ans)
