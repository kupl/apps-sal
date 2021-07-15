W, a, b = list(map(int, input().split()))

if a + W < b:
    print((abs(a + W - b)))
elif b + W < a:
    print((abs(b + W - a)))
else:
    print((0))

