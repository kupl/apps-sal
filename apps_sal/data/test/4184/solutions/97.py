n = int(input())
Ws = list(map(int, input().split()))
ans = float('inf')
for i in range(n):
    ans = min(ans, abs(sum(Ws[:i]) - sum(Ws[i:])))
print(ans)
