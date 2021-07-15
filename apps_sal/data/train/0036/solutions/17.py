# Codeforces contest 271d1 problem B

import bisect

n = int(input())
worms = [int(x) for x in input().split(' ')]
for i in range(n-1):
    worms[i+1] += worms[i]

m = int(input())
v = [int(x) for x in input().split(' ')]
[(lambda x: print(bisect.bisect_left(worms, x)+1))(x) for x in v]



