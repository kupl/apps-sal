#!/usr/bin/env python3
from collections import Counter
import sys
sys.setrecursionlimit(10**6)


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

c = Counter(a)

c = list(c.most_common())
# c = c.most_common()
len_c = len(c)
# print(len_c)
# print(c)
ans = 0
while(len_c-k > 0):
    # print(len_c-k)
    # print()
    # print(k)
    i, j = c.pop()
    len_c -= 1
    ans += j
print(ans)

