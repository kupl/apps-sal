n, dis = map(int,input().split())
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if (a**2 + b**2)**(1/2) <= dis:
        ans += 1
        
print(ans)
