N = int(input())
W = [int(n) for n in input().split()]
ans = 10**9
for t in range(1, N):
    ans = min(ans, abs(sum(W[:t]) - sum(W[t:])))
print(ans)
