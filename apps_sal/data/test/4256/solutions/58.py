(a, b, c) = map(int, input().split())
y = 0
for i in range(1000):
    b = b - a
    if b >= 0:
        y = y + 1
        if y == c:
            print(y)
            break
    else:
        print(y)
        break
