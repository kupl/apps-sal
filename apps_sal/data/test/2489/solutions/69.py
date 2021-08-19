n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[-1]
dp = [0 for _ in range(x + 1)]
for b in a:
    y = b
    while y <= x:
        dp[y] += 1
        y += b
ans = 0
for c in a:
    if dp[c] == 1:
        ans += 1
print(ans)
