(a, b, c, k) = list(map(int, input().split()))
if k <= a + b:
    print(min(a, k))
else:
    print(a - (k - (a + b)))
