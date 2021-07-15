N,M = map(int,input().split())
ans = int(M**0.5+10)*[N-1]
mod = 10**9+7
p = 2
O = M

while p<=O**0.5:
  if M%p == 0:
    M = M//p
    ans[p] += 1
  else:
    p+=1
    
if M!=1:
  ans[-1]+=1

out = 1
for r in ans:
  hoge = 1
  for i in range(min(N-1,r-N+1)):
    hoge*=r-i
    hoge//=i+1
  out*=hoge
  out%=mod

print(out)
