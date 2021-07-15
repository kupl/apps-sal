N,M=map(int,input().split())

if N >= 2*M:
  print(M//2)
  return
  
def f(x):
  return max(min(N+x, (M-2*x)//2),0)
  
delta = [-3,-2,-1,0,1,2,3]
x = (M-2*N)//4

ans = 0
for i in range(7):
  x_ = max(0,x+delta[i])
  ans = max(ans,f(x_))

print(ans)
