import heapq as h
q_num=int(input())
bsum=0
high=[]
low=[]
asum=0
for iii in range(q_num):
  q=[int(_) for _ in input().split()]
  if q[0]==1:
    bsum+=q[2]
    if len(low)==0:
      h.heappush(low,-q[1])
    else:
      asum+=abs(q[1]+low[0])
      if -low[0]>=q[1]:
        h.heappush(low,-q[1])
      else:
        h.heappush(high,q[1])
      
    if len(low)>=len(high)+2:
      ltoh=h.heappop(low)
      h.heappush(high, -ltoh)
    elif len(high)>=len(low)+1:
      ltoh=h.heappop(high)
      asum+=-low[0]-ltoh
      h.heappush(low, -ltoh)
  else:
    print(-low[0],asum+bsum)
