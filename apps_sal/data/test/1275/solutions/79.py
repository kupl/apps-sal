n,k = list(map(int,input().split()))
ans = 0

# x = a + b としてループ
for x in range(2,2*n+1):
    if 1 < x - k <= 2*n:
        ans += min(x-1, 2*n+1-x) * min(x-k-1, 2*n+1-x+k)

print(ans)

