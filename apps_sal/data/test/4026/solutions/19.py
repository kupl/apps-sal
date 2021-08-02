# cook your dish here
# code
#    ___________________________________
#   |                                   |
#   |                                   |
#   |        _,     _   _     ,_        |
#   |    .-'` /     \'-'/     \ `'-.    |
#   |   /    |      |   |      |    \   |
#   |  ;      \_  _/     \_  _/      ;  |
#   | |         ``         ``         | |
#   | |                               | |
#   |  ;    .-.   .-.   .-.   .-.    ;  |
#   |   \  (   '.'   \ /   '.'   )  /   |
#   |    '-.;         V         ;.-'    |
#   |        `                 `        |
#   |                                   |
#   |___________________________________|
#   |                                   |
#   |  Author      :   Ramzz            |
#   |  Created On  :   21-07-2020       |
#   |___________________________________|
#
#    _ __ __ _ _ __ ___  ________
#   | '__/ _` | '_ ` _ \|_  /_  /
#   | | | (_| | | | | | |/ / / /
#   |_|  \__,_|_| |_| |_/___/___|
#

import math
import collections
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr
import heapq as hq
setrecursionlimit(2**20)

t = 1
t = int(stdin.readline())

for _ in range(t):
    #n = int(stdin.readline())
    #s = stdin.readline().strip('\n')
    n, m = list(map(int, stdin.readline().rstrip().split()))
    chk = False
    for i in range(n):
        r1 = list(map(int, stdin.readline().rstrip().split()))
        r2 = list(map(int, stdin.readline().rstrip().split()))

        if(r1[1] == r2[0]):
            chk = True

    if(m % 2 == 1):
        print('NO')
        continue
    if(chk):
        print('YES')
    else:
        print('NO')
