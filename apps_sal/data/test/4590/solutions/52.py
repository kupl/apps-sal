# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
n, m, k = list(map(int, input().split()))
A = list(accumulate(list(map(int, input().split()))))
B = list(accumulate(list(map(int, input().split()))))
A=[0]+A
B=[0]+B
ans = []
for i in range(n+1):
    c = bisect_right(B, k-A[i])-1
    if c!=-1:
        ans.append(c+i)
print((max(ans)))

