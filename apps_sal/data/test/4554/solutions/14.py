W, a, b = map(int, input().split())
if b + W < a:
    print(a - (b + W))
elif a + W < b:
    print(b - (a + W))
else:
    print(0)
