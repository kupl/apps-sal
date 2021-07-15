n = int(input())
ans = 0
for i in range(100001):
    if i **2 <= n:
        ans = i**2
    
print(ans)

