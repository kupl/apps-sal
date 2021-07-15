N,K=map(int,input().split())
ans=0
if K==0:
  print(N*N)
  return
for b in range(K+1,N+1):
  _=(N//b)*(b-K)+max(0,(N%b)-K+1)
  ans+=_
  #print(b,_)
print(ans)
