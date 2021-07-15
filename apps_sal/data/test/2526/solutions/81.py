import heapq

x,y,a,b,c=list(map(int,input().split()))
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

ans=[]
for i in range(x):
  ans.append(p[i])
  
for j in range(y):
  ans.append(q[j])
  
ans.sort()

heapq.heapify(ans)

for j in range(c):
  min_a=heapq.heappop(ans)
  if min_a<=r[j]:
    heapq.heappush(ans,r[j])
  else:
    heapq.heappush(ans,min_a)
    break
    
print((sum(ans)))



