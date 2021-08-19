for i in range(int(input())):
    (a, b, x, y) = list(map(int, input().split()))
    print(max(a * max(y, b - y - 1), b * max(x, a - x - 1)))
