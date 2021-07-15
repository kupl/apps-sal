H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

ans=[]
for i in range(N):
  ans.extend([i+1]*a[i])
  
for i in range(H):
  if i % 2 == 0:
    print(*ans[i*W:(i+1)*W])
  else:
    print(*ans[i*W:(i+1)*W][::-1])
