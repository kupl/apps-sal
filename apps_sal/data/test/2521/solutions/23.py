from heapq import heapify,heappop,heappush
N=int(input())
a=list(map(int,input().split()))
ans=-10**18
a_neg=[-x for x in a]
af=a[:N]
ae=a_neg[2*N:]
f_sum=[sum(af)]
e_sum=[sum(ae)]

heapify(af)
for aa in a[N:2*N]:
  heappush(af,aa)
  t=heappop(af)
  f_sum.append(f_sum[-1]+aa-t)

heapify(ae)
for aa in reversed(a[N:2*N]):
  heappush(ae,-aa)
  t=heappop(ae)
  e_sum.append(e_sum[-1]-aa-t)

for f,e in zip(f_sum,reversed(e_sum)):
  ans=max(ans,f+e)

print(ans)
