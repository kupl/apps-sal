(W, a, b) = map(int, input().split())
if a - W <= b <= a + W:
    print(0)
elif b + W < a:
    print(a - (b + W))
else:
    print(b - (a + W))
