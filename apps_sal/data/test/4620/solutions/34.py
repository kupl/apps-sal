n=int(input())
yo=[]
for _ in range(n-1):
  a=list(map(int,input().split()))
  yo.append(a)
  
def ans(x):
  if x==n-1:
    return 0
  else:
    t=0
    for i in range(x,n-1):
      if t<=yo[i][1]:
        t=yo[i][1]+yo[i][0]
      else:
        s=t-yo[i][1]
        if s%yo[i][2]==0:
          t=t+yo[i][0]
        else:
          mo=s%yo[i][2]
          t=t+yo[i][2]-mo+yo[i][0]
    return t
    
for j in range(n):
  print((ans(j)))
        

