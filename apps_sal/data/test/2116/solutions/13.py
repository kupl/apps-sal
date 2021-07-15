n,m,k=list(map(int,input().split()))
p=list(map(int,input().split()))
p.reverse()
ans=0
for i in range(n):
    z=list(map(int,input().split()))
    for j in z:
        v=0
        for k in range(len(p)-1,-1,-1):
            v+=1
            if p[k]==j:
                ans+=v
                p.pop(k)
                p.append(j)
                break
print(ans)

