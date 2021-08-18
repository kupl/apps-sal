a, b, x, y = list(map(int, input().split()))

if a == b:
    ans = x
else:
    dif = abs(a - b)
    if a < b:
        ans = x + min(2 * x, y) * dif
    else:
        ans = x + min(2 * x, y) * (dif - 1)
print(ans)
