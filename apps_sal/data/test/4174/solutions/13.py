n,x=map(int,input().split())
l=list(map(int,input().split()))+[10**5]

d,cnt=0,0
while d<=x and cnt<n+1:
  d+=l[cnt]
  cnt+=1

print(cnt)
