n = int(input())
w = list(map(int, input().split()))
s = sum(w)
ans = float('inf')
for i in range(n):
    ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
print(ans)
