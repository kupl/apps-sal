(a, b) = map(int, input().split())
if a >= 2 and b >= 2:
    print((a - 2) * (b - 2))
elif a == 1 and b == 1:
    print(1)
else:
    print(a * b - 2)
