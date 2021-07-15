a, b, c = sorted(map(int, input().split()))
k = (c - a) // 2
if ((c - a) + (c - b)) % 2:
    print((((c - a) + (c - b)) // 2 + 2))
else:
    print((((c - a) + (c - b)) // 2))




