a, b = map(int, input().split())
if a == b:
    print(2 * a)
elif abs(a - b) == 1:
    print(a + b)
elif abs(a - b) >= 2:
    if a > b:
        print(a + (a - 1))
    else:
        print(b + (b - 1))
