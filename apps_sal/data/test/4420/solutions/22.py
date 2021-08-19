for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    can = c % a
    if can >= b:
        print(c // a * a + b)
    else:
        print((c // a - 1) * a + b)
