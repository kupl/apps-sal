n = int(input())
W = list(map(int, input().split()))

S1, S2 = 0, 0
ans = float("inf")
for i in range(1, n):
    S1, S2 = W[:i], W[i:]
    tmp = abs(sum(S1)-sum(S2))
    ans = min(ans, tmp)
print(ans)
