a, b, k = map(int, input().split())

if a >= k:
    print(a - k, b)
elif b >= k - a:
    print(0, b - k + a)
else:
    print(0, 0)
