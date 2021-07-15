#abc_155_d
import numpy as np
n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = np.array(a)
a.sort()

plus = a[a>0]
zero = a[a==0]
minus= a[a<0]

left = -10**18
right = 10**18

while left+1 < right:
    mid = (left+right)//2
    cnt = 0
    
    if mid >=0:
        cnt += len(zero) * n
    
    cnt += a.searchsorted(mid//plus, side="right").sum()
    cnt += (n - a.searchsorted(-(-mid//minus), side="left")).sum()
    cnt -= np.count_nonzero(a*a <= mid)
    cnt /= 2
    
    if cnt >= k:
        right = mid
    if cnt < k:
        left=mid
        
print(right)
