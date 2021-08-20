(a, b) = map(int, input().split())
if a == b:
    print(a + b)
elif a - b >= 1:
    print(a + a - 1)
else:
    print(b + b - 1)
