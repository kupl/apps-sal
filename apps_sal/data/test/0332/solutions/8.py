'''input
3 3
1 2 3
4 5 6
7 8 9
1 4 7
2 5 6
3 8 9
'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n, m = ri()

mat = []
mat1 = []
for i in range(n):
    mat.append(ri())
for i in range(n):
    mat1.append(ri())
one = dd(list)
for i in range(n):
    for j in range(m):
        one[i + j].append(mat[i][j])

two = dd(list)
for i in range(n):
    for j in range(m):
        two[i + j].append(mat1[i][j])

for i in one:
    one[i].sort()
for i in two:
    two[i].sort()

f = 1
for i in one:
    if one[i] != two[i]:
        f = 0
if f:
    print("YES")
else:
    print("NO")
