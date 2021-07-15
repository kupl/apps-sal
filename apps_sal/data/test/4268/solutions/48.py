n,d =map(int,input().split())
l= [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        a = 0
        for k in range(d):
            a += (l[i][k] - l[j][k])**2
        a **=0.5
        if a.is_integer():
            ans +=1
print(ans)
