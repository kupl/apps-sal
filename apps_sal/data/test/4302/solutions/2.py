a, b = map(int, input().split())
if a == b:
    print(2 * a)
elif a > b:
    print(a + a - 1)
else:
    print(b + b - 1)
