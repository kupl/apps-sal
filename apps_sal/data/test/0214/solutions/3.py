s=input()
t=input()
dp=[]
n=len(s)
a=[]
b=[]
for i in range(n+1):
    dp.append((0,0))
for i in range(n):
    a.append(s[i])
    b.append(t[i])
ans=0
for i in range(n):
    if a[i]=='0' and b[i]=='0':
        if i>0 and (a[i-1]=='0' or b[i-1]=='0'):
            if a[i-1]=='0':
                a[i]=b[i]=a[i-1]='X'
                ans+=1
            elif b[i-1]=='0':
                a[i]=b[i]=b[i-1]='X'
                ans+=1
        elif i+1<n:
            if a[i+1]=='0':
                a[i]=b[i]=a[i+1]='X'
                ans+=1
            elif b[i+1]=='0':
                a[i]=b[i]=b[i+1]='X'
                ans+=1
print(ans)

