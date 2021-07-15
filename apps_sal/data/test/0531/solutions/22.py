n=int(input().strip())
l=[int(x) for x in input().strip().split()]
if len(set(l))==1:
  print(n)
  print(*l)
  return
l.sort()
f=[0]*3
s=list(set(l))
s.sort()
if len(s)==2 and s[1]-s[0]==1:
    print(n)
    print(*l)
    return
if len(s)==2:
    s.append(s[-1])
    s[1]=(s[0]+1)
for i in range(3):
    f[i]=l.count(s[i])
if f[1]>(min(f[0],f[2])*2):
    ans=f[1] - f[1]%2 
    ans=n-ans
    flag=0
    if f[1]%2==1:
        flag=1 
    f[0]+=(f[1]//2)
    f[2]+=(f[1]//2)
    f[1]=flag
    print(ans)
    for i in range(3):
        print((str(s[i])+" ")*f[i],end="")
else:    
    ans=f[1]+max(f[0],f[2])-min(f[0],f[2])
    f[1]+=(min(f[0],f[2])*2)
    f[0],f[2]=f[0]-min(f[0],f[2]),f[2]-min(f[0],f[2])
    print(ans)
    for i in range(3):
        print((str(s[i])+" ")*f[i],end="")
    print("")
