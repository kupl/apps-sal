a=list(input())
b=list(input())
n=len(a)
ans=0
for i in range(n-1):
    if(a[i+1]=='0' and a[i]=='0' and b[i]=='0'):
        ans+=1
        a[i]=a[i+1]=b[i]='X'
    elif(b[i+1]=='0' and a[i]=='0' and b[i]=='0'):
        ans+=1
        a[i]=b[i+1]=b[i]='X'
    elif(b[i+1]=='0' and a[i+1]=='0' and b[i]=='0'):
        ans+=1
        a[i+1]=b[i+1]=b[i]='X'
    elif(b[i+1]=='0' and a[i+1]=='0' and a[i]=='0'):
        ans+=1
        a[i+1]=b[i+1]=a[i]='X'
print(ans)
