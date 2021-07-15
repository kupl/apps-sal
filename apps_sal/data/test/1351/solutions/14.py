# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353 
# INF = 1000000000000000000000

# from sys import stdout
# from heapq import heappush, heappop
from collections import defaultdict
# from collections import deque  

# from math import sqrt    
# from math import gcd
# from math import log2

t = 1# int(input())

for test in range(t):
    # n = int(input())
    found = 0
    l, r = list(map(int, input().split()))
    for i in range(l, r+1):
        a = list(str(i))
        if len(set(a)) == len(a):
            print(i)
            found = 1
            break
    if found==0:
        print(-1)


    
    

