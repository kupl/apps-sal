n=int(input())
lr=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
  ans+=(lr[i][1]-lr[i][0]+1)
print(ans)
