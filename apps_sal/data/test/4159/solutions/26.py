a, b, k = map(int, input().split())
if a >= k:
    print(a - k, b)
elif a < k <= a + b:
    print(0, a + b - k)
else:
    print(0, 0)
