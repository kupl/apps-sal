import bisect

n,m = map(int,input().split())

x,y,z = [],[],[]

for _ in range(n):
    i,j,k = map(int,input().split())
    x.append(i)
    y.append(j)
    z.append(k)

ans = 0

for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            li = []
            for l in range(n):
                li.append(x[l]*i+y[l]*j+z[l]*k)
            li.sort(reverse=True)
            ans = max(ans,sum(li[:m]))

print(ans)
