r, d, x = map(int, input().split())
for i in range(10):
    y = r * x - d
    print(y)
    x = y
