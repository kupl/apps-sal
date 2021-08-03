k, s = list(map(int, input().split()))

count = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if z < 0 or z > k:
            continue
        count += 1
        # print(x, y, z)

print(count)
