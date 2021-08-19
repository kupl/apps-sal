#import sys
#sys.stdin = open("python/in", "r")
#from collections import defaultdict
#import numpy as np
#import array as rr
#arr = rr.array('q')

n = int(input())
#n, m = [int (i) for i in input().split(" ")]
ans = {}
arr = []
for con in range(1, 2 * n):
    str = [int(i) for i in input().split(" ")]
    arr.extend([(str[i], i, con) for i in range(len(str))])
arr.sort()
arr.reverse()
for s, a, b in arr:
    if a in ans.keys() or b in ans.keys():
        continue
    ans[a] = b + 1
    ans[b] = a + 1

for i in range(2 * n):
    print(ans[i], end=' ')
