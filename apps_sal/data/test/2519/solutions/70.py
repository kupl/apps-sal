n,k = map(int,input().split())
p = list(map(int,input().split()))

for i in range(n):
    p[i] = (1+p[i]) / 2
    
res = sum(p[:k])
ans = res
    
for i in range(n-k):
    res += -p[i] + p[i+k]
    ans = max(ans,res)
    
print(ans)
