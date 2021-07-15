n,d=list(map(int, input().rstrip().split()))
m=[]
for _ in range(n):
    arr=list(map(int, input().rstrip().split()))
    m.append(arr)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        a = 0
        for k in range(d):
            a += (m[i][k] - m[j][k])**2
        x = int(a**(1/2))
        if x**2 == a:
            ans+=1
print(ans)

