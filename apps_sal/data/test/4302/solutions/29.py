(a, b) = map(int, input().split())
if a >= b + 2:
    print(a + a - 1)
elif a == b + 1 or b == a + 1 or a == b:
    print(a + b)
elif a + 2 <= b:
    print(b + b - 1)
