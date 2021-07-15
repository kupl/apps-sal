from math import ceil
N,A,B=map(int,input().split())
if N+1<A+B or A*B<N:
  print(-1)
  return

t=N//B
s=[]
while N>0:
  if N==A:
    s.append(list(range(1,N+1)))
    break
  if N-B>=A-1:
    s.append(list(range(N,N-B,-1)))
    N-=B
    A-=1
    continue  
  s.append(list(range(N,A-1,-1)))
  s.append(list(range(1,A)))
  break
ans=[]
s.reverse()
for a in s:
  ans.append(' '.join(map(str,a)))
 
print(' '.join(ans))
