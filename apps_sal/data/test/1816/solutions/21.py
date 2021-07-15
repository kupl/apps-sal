from bisect import bisect
from itertools import permutations,combinations
n=int(input())
a=list(map(int,input().split()))

cnt=1
b = []
for x in a:
    b.append([x,cnt])
    cnt+=1
b.sort()
res = 0
for i in range(1,n):
    res+=abs(b[i][1]-b[i-1][1])
print(res)
