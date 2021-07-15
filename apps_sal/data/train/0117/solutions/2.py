import math
from collections import deque
from sys import stdin, stdout, setrecursionlimit
from string import ascii_letters
letters = ascii_letters[:26]
from collections import defaultdict
#from functools import reduce
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    horizontal = [list(map(int, input().split())) for i in range(n)]
    vertical = [list(map(int, input().split())) for i in range(m)]
    vals = vertical[0]
    first = vals[0]
    pos = 0
    
    for i in horizontal:
        for g in range(m):
            if i[g] == first:
                pos = g
    
    path = {}
    order = {}
    for ind, i in enumerate(vals):
        path[i] = ind
    for ind, i in enumerate(horizontal):
        order[path[i[pos]]] = ind

    for i in range(len(order)):
        print(*horizontal[order[i]])


