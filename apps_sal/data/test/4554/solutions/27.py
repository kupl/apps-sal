W, a, b = list(map(int, input().split()))

if a <= b <= a + W or a <= b + W <= a + W:
    print((0))
else:
    print((min(abs(a + W - b), abs(b + W - a))))

