(a, b, c, d) = list(map(int, input().split()))
(a, b, c) = sorted((a, b, c))
ans = 0
if b - a < d:
    ans += d - (b - a)
if c - b < d:
    ans += d - (c - b)
print(ans)
