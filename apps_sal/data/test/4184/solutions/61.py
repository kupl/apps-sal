n = int(input())
w = list(map(int, input().split()))
ans = 10**4
for i in range(n):
    x = abs(sum(w[:i + 1]) - sum(w[i + 1:n]))
    ans = min(ans, x)
print(ans)
