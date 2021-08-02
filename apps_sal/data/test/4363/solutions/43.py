k, s = list(map(int, input().split()))
counter = 0
for x in range(k + 1):
    for y in range(x, k + 1):
        z = s - x - y
        if y <= z <= k:
            if x == y == z:
                counter += 1
            elif x == y or y == z:
                counter += 3
            else:
                counter += 6

print(counter)
