(a, b, c, k) = list(map(int, input().split()))
if k <= a:
    print(k)
if a < k <= a + b:
    print(a)
if a + b < k <= a + b + c:
    print(a - (k - (a + b)))
