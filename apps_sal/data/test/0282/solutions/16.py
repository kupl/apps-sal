import sys
n,d=list(map(int,sys.stdin.readline().split()))
s=list(input())
a=[]
for i in range(1,len(s)):
    if(s[i]=='1'):
        a.append(i)

mina=None
c=d
x=0
flag=0
if(len(a)==1 and a[0]>d):
    print(-1)
    return
if(len(a)==1 and a[0]<=d):
    print(1)
    return
for i in range(0,len(a)-1):
    if(a[i]>c):
        flag=1
        break
    if(a[i]<=c and a[i+1]>c):
        x+=1
        c=a[i]+d
    
if(abs(a[i]-a[len(a)-1])<=d and flag==0):
    x+=1
else:
    x=0
if(x==0):
    print(-1)
    return
print(x)


