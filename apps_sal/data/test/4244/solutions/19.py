n = int(input())
x = list(map(int, input().split()))

ans = 1000000
for i in range(100):
    tmp = 0
    for j in range(n):
        tmp += (x[j]-(i+1))**2
        
    ans = min(ans, tmp)
    
print(ans)
