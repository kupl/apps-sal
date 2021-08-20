(N, K) = map(int, input().split())
H = sorted([int(i) for i in input().split()])
ans = 0
for i in range(N - K):
    ans += H[i]
print(ans)
