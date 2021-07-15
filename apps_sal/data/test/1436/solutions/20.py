n = int(input())
police = 0
ans = 0
a = list(map(int, input().split()))
for i in range(n):
    q = a[i]
    if q < 0:
        if police > 0:
            police -= 1
        else:
            ans += 1
    else:
        police += q
print(ans)    
