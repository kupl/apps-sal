N = int(input())
W = list(map(int, input().split()))
ans = 9899
for i in range(N):
    ans = min(ans, abs(sum(W[0:i]) - sum(W[i:N])))
print(ans)
