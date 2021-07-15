p=int(input())
if p == 2:
    print(1)
    return
ans=0
for x in range(1,p):
    m=x%p
    if m==1:
        if x==2:
            q=True
        else:
            q=False
    else:
        q=False
        for i in range(2,p):
            m=(m*x)%p
            if m==1:
                if i==p-1:
                    q=True
                break
    ans+=q
print(ans)
    

