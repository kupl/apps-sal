n,s,t = input().split()
n=int(n)
s=int(s)
t=int(t)
l=input().split()
for i in range(n):
    l[i]=int(l[i])
j=0
i=s
flag=0
if(s==t):
    flag=1
while(j<n and flag!=1):
    if(i==l[i-1]):
        if(i==t):
            flag=1
            break
        break
    i=l[i-1]
    if(i==t):
        flag=1
        j+=1
        break
    j+=1

if(flag):
    print(j)
else:
    print(-1)

