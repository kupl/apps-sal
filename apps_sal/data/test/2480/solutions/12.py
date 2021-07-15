n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]
mp={0:1}
ans=0
for t in range(n):
  i=a[t]
  
  if t>=k-1:
    mp[dp[-k]]-=1  
    
  num=(dp[-1]+i-1)%k
  if num in mp.keys():
    ans += mp[num]
    mp[num] += 1
  else:
    mp[num] = 1
  dp.append(num)

print(ans)
