a, b = map(int, input().split())
for x in range(-100, 101):
    for y in range(-100, 101):
        if x + y == a and x - y == b:
            print(x, y)
            break
