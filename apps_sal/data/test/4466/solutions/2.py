(x, y, z) = map(int, input().split())
for i in range(100000):
    if (i + 1) * z + i * y > x:
        print(i - 1)
        break
