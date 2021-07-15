# cook your dish here
# import sys
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

import math
import collections
from sys import stdin,stdout,setrecursionlimit
import bisect as bs
T = int(stdin.readline())

for _ in range(T):
    # n = int(stdin.readline())
    a,b,c,d = list(map(int,stdin.readline().split()))
    # h = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    # s = stdin.readline().strip('\n')
    if(b >= a):
        print(b)
        continue
    rem = a-b
    if(c-d <= 0):
        print(-1)
        continue
    ans = b+c*((rem//(c-d))+(1 if rem % (c-d) != 0 else 0))
    print(ans)

