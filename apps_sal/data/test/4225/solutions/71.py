(a, b, c, k) = map(int, input().split())
if k <= a:
    print(k)
elif k <= a + b:
    print(a)
elif a <= k - a - b:
    print(-1 * (k - a - b - a))
elif a > k - a - b:
    print(a - (k - a - b))
