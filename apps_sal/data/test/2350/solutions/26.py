
for _ in range(int(input())):
    x, y, x2, y2 = list(map(int, input().split()))
    a = x2 - x
    b = y2 - y
    print(a**2 + 1 + (b - a) * a)
