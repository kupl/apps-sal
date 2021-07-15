n = int(input())
l = list(map(int,input().split()))

ans = 0
for c in range(1,n):
    now = 0
    pas = set()
    for k in range(1,n):
        if k * c > n-1 or n-1-k*c <= c:
            break
        if n-1-k*c in pas or k*c in pas or n-1 == 2*k*c:
            break 
        now += l[n-1-k*c] + l[k*c]
        pas.add(n-1-k*c)
        pas.add(k*c)
        ans = max(ans,now)
        
print(ans)

