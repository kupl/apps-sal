N = int(input())
W = list(map(int, input().split()))
total = sum(W)
former = 0
ans = total
for i in range(N - 1):
    former += W[i]
    latter = total - former
    ans = min(ans, abs(former - latter))
print(ans)
