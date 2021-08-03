for nt in range(int(input())):
    a, b, x, y = map(int, input().split())
    a1 = max(x, 0) * b
    a2 = (a - x - 1) * b
    a3 = (y) * a
    a4 = (b - y - 1) * a
    print(max(a1, a2, a3, a4))
