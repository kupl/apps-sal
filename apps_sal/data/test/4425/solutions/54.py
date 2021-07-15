N,K = map(int, input().split())
 
ans = 0
 
for i in range(1, N+1):
    j = 1/N
    while i < K:
        i *= 2
        j /= 2
    ans += j
 
print(ans)
