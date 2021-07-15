a, b, c, k = list(map(int, input().split()))

s = []
x = 0

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
elif k <= a + b + c:
    print((2 * a + b - k))
else:
    print((a - c))

