n = int(input())
p = list(map(int, input().split()))
swapped=[0] * (n-1)
noc=1

for now in range(0,n-1):
  if now>0 and swapped[now-1]==0:
    print(-1)
    return
  for i in range(now,n):
    if (p[i]-1==now):
      if(p[i]-1<i):
        for j in range(i-1,p[i]-2,-1):
          if swapped[j]!=0:
            print(-1)
            return
          p[j],p[j+1]=p[j+1],p[j]
          swapped[j]=noc  
          noc+=1
      break
if swapped[n-2]==0:
  print(-1)
  return
for i in range(0,n-1):
  print(swapped[i])
