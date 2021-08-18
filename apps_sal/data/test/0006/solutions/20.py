'''input
3
3 10
6 3
8 2
1 4
4 10
4 1
3 2
2 6
1 100
2 15
10 11
14 100

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


for _ in range(ri(1)):
    n, curr = ri()
    a = []
    for i in range(n):
        a.append(ri())
    a.sort(key=lambda x: -x[0] + x[1])

    hey = a[0][0] - a[0][1]
    take = -1
    b = []
    for i, j in a:
        take = max(take, i)
        b.append(i - j)
    b.sort(reverse=True)
    ans = 0
    curr = curr - take
    if curr <= 0:
        print(1)
    else:
        if b[0] <= 0:
            print(-1)
        else:
            hey = curr // b[0]
            if curr % b[0] == 0:
                print(hey + 1)
            else:
                print(hey + 2)
