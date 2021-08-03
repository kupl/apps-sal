k, s = map(int, input().split())
count = 0

if k * 3 == s:
    print(1)
    return

for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if z >= 0 and z <= k:
            count += 1
print(count)
