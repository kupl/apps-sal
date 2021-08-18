W, a, b = list(map(int, input().split()))

ans1 = b - (a + W)
ans2 = a - (b + W)

if a + W < b or b + W < a:
    print((min(abs(ans1), abs(ans2))))
else:
    print((0))
