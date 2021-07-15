from collections import deque
#from heapq import heapify, heappop, heappush
from bisect import bisect_left
#from math import gcd
#from decimal import Decimal
#mod = 1000000007
#mod = 998244353
N = int(input())
#N, K = map(int, input().split())
P = list(map(int, input().split()))
#flag = True
big = []
for k in range(N):
  big.append((P[k], k+1))
big.sort(key=lambda x: x[0], reverse=True)
big = deque(big)
item = big.popleft()
done = [0,0,item[1],N+1,N+1]
ans = 0
while big:
  item = big.popleft()
  index = item[1]
  num = item[0]
  i = bisect_left(done, index)
  done.insert(i, index)
  ans += num*((done[i+2]-done[i+1])*(index - done[i-1])+ (done[i-1]-done[i-2])*(done[i+1]-index))
print(ans)
#print('Yes')
#print('No')

