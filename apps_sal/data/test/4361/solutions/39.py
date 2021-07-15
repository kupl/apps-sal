n, k = map(int, input().split())
hl = sorted(list(int(input()) for _ in range(n)))

ans = 1001001001
for i in range(n-k+1):
    ans = min(hl[i+k-1]-hl[i], ans)

print(ans)
