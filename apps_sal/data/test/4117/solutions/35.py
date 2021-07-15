n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:continue
        for k in range(j+1,n):
            if l[j]==l[k]:continue
            if l[i]+l[j]>l[k]:ans+=1
print(ans)
