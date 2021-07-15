c = list(map(int,input().split()))
total = sum(c)
ans = "No"

for i in range(8):
    eat = 0

    for j in range(4):
        if (i>>j)&1:
            eat += c[j]
            
    if eat == total - eat:
        ans = "Yes"
        
print(ans)
