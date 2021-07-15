n=2*int(input())
w=sorted(map(int,input().split()))
r=10000
for i in range(n):
    for j in range(i):
        u=[w[k] for k in range(n) if i!=k!=j]
        r=min(r,sum(u[i+1]-u[i] for i in range(0,n-3,2)))
print(r)

