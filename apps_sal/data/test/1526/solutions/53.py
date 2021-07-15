a=list(map(int,input().split()))
cnt=0
for i in range(3):
  if a[i]%2==1:
    cnt+=1
if cnt==0 or cnt==3:
  print(((3*max(a)-sum(a))//2))
elif cnt==1 and max(a)%2==1 or cnt==2 and max(a)%2==0:
  print(((max(a)-a[0])//2+(max(a)-a[1])//2+(max(a)-a[2])//2+1))
else:  
  print(((max(a)+1-a[0])//2+(max(a)+1-a[1])//2+(max(a)+1-a[2])//2+1))

