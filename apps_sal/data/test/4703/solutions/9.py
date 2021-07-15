a=list(input())
ans=0
for i in range(2**(len(a)-1)):
    s=a[0]
    for j in range(len(a)-1):
        if i%2:s+='+'
        s+=a[j+1]
        i//=2
    ans+=eval(s)
print(ans)
