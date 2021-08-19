for _ in range(int(input())):
    (a, b, x, y) = list(map(int, input().split()))
    num1 = x * b
    num2 = y * a
    num3 = (a - x - 1) * b
    num4 = (b - y - 1) * a
    print(max(num2, num1, num3, num4))
