#import sys
#sys.stdin = open("python/in", "r")
#from collections import defaultdict
#import numpy as np
#import array as rr
#arr = rr.array('q')

n = int(input())
#n, m = [int (i) for i in input().split(" ")]
ans = 0
while n > 0:
    if n%2 == 1:
        ans += 1
    n = n//2

print(ans)
