(x, k, d) = map(int, input().split())
ans = 0
if x < 0:
    x *= -1
if k * d <= x:
    ans = x - k * d
elif x < k * d:
    k -= x // d
    x -= x // d * d
    ans = x if k % 2 == 0 else x - d
print(ans if 0 <= ans else -ans)
