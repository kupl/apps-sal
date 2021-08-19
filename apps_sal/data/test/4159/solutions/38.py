(a, b, k) = map(int, input().split())
if a + b <= k:
    print(0, 0)
elif a >= k:
    print(a - k, b)
else:
    print(0, b - k + a)
