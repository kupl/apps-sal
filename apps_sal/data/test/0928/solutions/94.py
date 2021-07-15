n,k=map(int,input().split())

a=list(map(int,input().split()))

u=[0]

ui=0

for i in range(n):
  ui+=a[i]
  u.append(ui)


left=0
right=1


ans=0

while right<=n:
  s=u[right]-u[left]
  if s<k:
    right+=1
  else:
    ans+=n-right+1
    left+=1
    
print(ans)
