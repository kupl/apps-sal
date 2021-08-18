n = int(input())
a = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] += a[i] + s[i]
ans = float("inf")
for i in range(1, n):
    x = s[i]
    y = s[n] - s[i]
    ans = min(ans, abs(x - y))
print(ans)
