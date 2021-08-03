x, k, d = map(int, input().split())
if abs(x) > k * d:
    print(abs(x) - k * d)
else:
    kaisuu = abs(x) // d
    if k % 2 == kaisuu % 2:
        print(abs(x) % d)
    else:
        print(d - abs(x) % d)
