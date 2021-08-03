r, h = list(map(int, input().split()))
ans = (h // r) * 2
h %= r
if 2 * h < r:
    ans += 1
elif 2 * h < 1.732 * r:
    ans += 2
else:
    ans += 3
print(ans)
