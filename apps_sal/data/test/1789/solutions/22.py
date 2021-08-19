(a, b, x, y) = list(map(int, input().split()))
if a == b:
    print(x)
elif a < b:
    ans = min(y, 2 * x) * (b - a) + x
    print(ans)
else:
    ans = min(y, 2 * x) * (a - b - 1) + x
    print(ans)
