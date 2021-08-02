n, k = list(map(int, input().split()))
hl = sorted(list(int(input()) for _ in range(n)), reverse=True)
ans = 1001001001
for i in range(n - k + 1):
    ans = min(ans, hl[i] - hl[i + k - 1])
print(ans)
