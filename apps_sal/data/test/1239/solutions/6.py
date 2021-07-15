n=int(input())
a=[int(i) for i in input().split()]
a.sort()
res=[]
for i in range(n-1):
    res.append(abs(a[i]-a[i+1]))
m=min(res)
c=0
for x in sorted(res):
    if x==m:
        c+=1
    else:
        break
print(m,c)

