for t in range(int(input())):
    a, b, x, y = [int(i) for i in input().split()]
    l = max(x, a - 1 - x)
    h = max(y, b - 1 - y)
    print(max(l * b, h * a))
