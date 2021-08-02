k, s = list(map(int, input().split()))

sum = 0

for z in range(k + 1):
    for y in range(k + 1):
        if (s - y - z <= k and s - y - z >= 0):
            sum += 1

print(sum)
