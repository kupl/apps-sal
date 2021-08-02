a, b, c, k = list(map(int, input().split()))

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print((2 * a + b - k))
