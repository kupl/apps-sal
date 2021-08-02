'''input
3
5 3
7 18 3 14 1
5 4
1 2 3 4 5
6 2
1 2 8 4 10 2

'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from heapq import heappush as hpush
from heapq import heappop as hpop
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


for _ in range(int(input())):
    n, k = ri()
    a = ri()
    su = [0]
    for i in a:
        su.append(su[-1] + i)
    ans = []
    pre = 0
    for i in range(len(a)):
        pre += a[i]
        if len(ans) != k - 1 and pre % 2 == 1:
            ans.append(i + 1)
            pre = 0
    if pre % 2 == 1:
        ans.append(n)
        pre = 0

    if pre != 0 or len(ans) != k:
        print("NO")
    else:
        print("YES")
        print(*ans)
