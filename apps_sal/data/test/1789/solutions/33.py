(a, b, x, y) = map(int, input().split())
if a == b:
    print(x)
elif a < b:
    ans1 = (b - a) * y + x
    ans2 = (b - a) * x * 2 + x
    print(min(ans1, ans2))
else:
    ans1 = (a - b - 1) * y + x
    ans2 = (a - b - 1) * x * 2 + x
    print(min(ans1, ans2))
