(x, y, z) = list(map(int, input().split()))
i = 1
while True:
    if (y + z) * i + z > x:
        print(i - 1)
        break
    i += 1
