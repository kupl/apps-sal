n = int(input())
hs =list(map(int, input().split()))

ans = hs[-1]
for i in range(1,n):
    if hs[i] < hs[i-1]:
        ans += hs[i-1] -hs[i]
    else:
        continue
        
print(ans)
