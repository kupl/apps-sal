# c
x, k, d = map(int, input().split())
x = abs(x)
x1 = x // d
if k <= x1:
    ans = x - k * d
else:
    if (k - x1) % 2 == 0:
        ans = x % d
    else:
        ans = d - x % d

print(ans)
