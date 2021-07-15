from heapq import heappop, heappush
Q = int(input())
maxh = []
minh = []
sum1 = sum2 = b = med = 0
for i in range(Q):
  q = list(map(int, input().split()))
  if q[0]==1:
    b += q[2]
    if len(maxh)==0 or q[1]<-maxh[0]:
      heappush(maxh, -q[1])
      sum1 += q[1]
      if len(maxh)>len(minh)+1:
        t = -heappop(maxh)
        heappush(minh, t)
        sum1 -= t
        sum2 += t
    else:
      heappush(minh, q[1])
      sum2 += q[1]
      if len(maxh)<len(minh):
        t = heappop(minh)
        heappush(maxh, -t)
        sum1 += t
        sum2 -= t
    med = -maxh[0]
  else:
    ans = len(maxh)*med-sum1+sum2-len(minh)*med+b
    print(med, ans)
