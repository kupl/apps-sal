x = int(input())
q = x // 11
ans = 2 * q
r = x % 11
if r > 6:
    ans += 2
if 0 < r <= 6:
    ans += 1
print(ans)
