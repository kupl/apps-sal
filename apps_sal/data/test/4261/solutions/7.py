a, b, c = list(map(int, input().split()))

if c <= a - b:
    print((0))
else:
    print((c - (a - b)))
