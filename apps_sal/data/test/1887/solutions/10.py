n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ans=[a[n-1],b[n-1]]
bans=[0,0]
for i in range(n-2,-1,-1):
  bans[0] = max(a[i]+ans[1],ans[0])
  bans[1] = max(b[i]+ans[0],ans[1])
  ans[0]=bans[0]
  ans[1]=bans[1]
  bans[0]=0
  bans[1]=0
print(max(ans))

