n,k = list(map(int, input().split()))
ans = 0
for i in range(2, 2*n+1):
    if 2 <= i-k <= 2*n:
        ans += max(0, min(i-1, n)-max(i-n, 1)+1)*max(0, min(i-k-1, n)-max(i-k-n, 1)+1)
print(ans)

