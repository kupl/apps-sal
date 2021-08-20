(k, s) = map(int, input().split())
count = 0
for x in range(k + 1):
    for y in range(x + 1):
        if x + y > s:
            continue
        else:
            z = s - x - y
            if z > x or z > y:
                continue
            if x == y == z:
                count += 1
            elif x == y or y == z or z == x:
                count += 3
            else:
                count += 6
print(count)
