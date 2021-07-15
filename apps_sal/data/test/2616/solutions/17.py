import sys
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')
 
import math
import collections
from sys import stdin,stdout,setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
MOD = 998244353
    
T = int(stdin.readline())
# T = 1

for _ in range(T):
    n = int(stdin.readline())
    # n,m = list(map(int,stdin.readline().split()))
    a = list(map(int,stdin.readline().split()))
    # q = int(stdin.readline())
    # b = list(map(int,stdin.readline().split()))
    # q = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    # s = stdin.readline().strip('\n')
    ind = -1
    for i in range(n):
        if(a[i] > 1):
            ind = i
            break
    if(ind == -1):
        if(n%2 == 0):
            print("Second")
        else:
            print("First")
        continue
    if(ind%2 == 0):
        print("First")
    else:
        print("Second")
