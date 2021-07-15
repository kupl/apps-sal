n=int(input())
a,d,f=[],0,0
for i in range(n-1):
    k,l=list(map(int,input().split()))
    a.append(k)
    a.append(l)
for i in range(len(a)):
    d=0
    for j in range(len(a)):
        if i!=j and a[i]==a[j]:d=d+1
    if d==0:f=f+1
print(f)

