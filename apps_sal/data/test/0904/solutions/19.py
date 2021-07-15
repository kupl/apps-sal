n=int(input())
l=list(map(str,input().strip().split(' ')))
ans=-1
for i in range(len(l)):
    c=0
    for j in l[i]:
        if ord(j)<=90 and ord(j)>=65:
            c+=1
    ans=max(c,ans)
print(ans)
