n = int(input())
b = list(map(int, input().split()))
d = {}
ans = 0
for i in range(n):
    diff = b[i] - i
    if diff not in d:
        d[diff] = 0
    d[diff] += b[i]
    ans = max(ans, d[diff])
print(ans)
