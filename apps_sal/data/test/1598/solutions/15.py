s=input()
n=len(s)
b=[0]*n
x=1
l=[]
for i in range(n):
    l.append(i)
while(x==1):
    x=0
    for i in range(len(s)-1):
        if(s[i]=='1' and s[i+1]=='0'):
            x=1
            b[int(l[i])]=1
            l[i]=l[i+1]=1000000
    s=s.replace("10","")
    l=list(set(l))
    if(x==1):
        l.remove(1000000)
print(*b,sep="")
