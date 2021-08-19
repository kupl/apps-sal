(a, b, x, y) = list(map(int, input().split()))
if a > b:
    if y >= 2 * x:
        ans = abs(a - b - 1) * 2 * x + x
    else:
        ans = abs(a - b - 1) * y + x
elif y >= 2 * x:
    ans = abs(a - b) * 2 * x + x
else:
    ans = abs(a - b) * y + x
print(ans)
