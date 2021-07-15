def read():
    return list(map(int,input().split()))
n,m=read()
x=read()
y=read()
i=0
j=0
s1=0
s2=0
ans=0
q=True
while not (i==n and j==m):
    s1+=x[i]
    i+=1
    while s1!=s2:
        if s1<s2:
            s1+=x[i]
            i+=1
        else:
            s2+=y[j]
            j+=1
    ans+=1
    s1=0
    s2=0
print(ans)


