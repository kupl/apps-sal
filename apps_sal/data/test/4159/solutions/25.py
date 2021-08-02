a, b, k = map(int, input().split())
if a <= k:
    if b <= k - a:
        print(0, 0)
    else:
        print(0, b - (k - a))
else:
    print(a - k, b)
