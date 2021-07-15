n,k=map(int,input().split())
a=list(map(int,input().split()))
from itertools import accumulate
ac=[0]+list(accumulate(a))
from bisect import bisect_left
count=0
for i in range(1,n+1):
    count+=(n-bisect_left(ac,k+ac[i-1])+1)
print(count)
