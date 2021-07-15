n=int(input())
alist=[list(map(int, input().split())) for i in range(n)]
alist.sort(key=lambda x:x[2],reverse=True)
for i in range(101):
  for j in range(101):
    h=abs(alist[0][0]-i)+abs(alist[0][1]-j)+alist[0][2]
    ans=True
    for k in range(n):
      if max((h-abs(alist[k][0]-i)-abs(alist[k][1]-j)),0)!=alist[k][2]:
        ans=False 
    if ans:
      ansx=i
      ansy=j
      ansh=h
print(ansx,ansy,ansh)
