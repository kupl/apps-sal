import heapq

n=int(input())
arr=list(map(int,input().split()))
q1=[]
tmp=0
for val in arr[:n]:
  heapq.heappush(q1,val)
  tmp+=val
sum1=[tmp]
for val in arr[n:2*n]:
  tmp=heapq.heappop(q1)
  if val>tmp:
    heapq.heappush(q1,val)
    sum1.append(sum1[-1]+(val-tmp))
  else:
    heapq.heappush(q1,tmp)
    sum1.append(sum1[-1])
q2=[]
tmp=0
for val in arr[2*n:]:
  heapq.heappush(q2,-val)
  tmp+=val
sum2=[tmp]
for val in arr[2*n-1:n-1:-1]:
  tmp=-heapq.heappop(q2)
  if val<tmp:
    heapq.heappush(q2,-val)
    sum2.append(sum2[-1]+(val-tmp))
  else:
    heapq.heappush(q2,-tmp)
    sum2.append(sum2[-1])
sum2=sum2[::-1]
ans=-10**18
for i in range(n+1):
  tmp=sum1[i]-sum2[i]
  ans=max(ans,tmp)
print(ans)
