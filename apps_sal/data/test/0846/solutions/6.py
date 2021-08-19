[n, m] = list(map(int, input().split()))
lamps = [0] * n
for x in map(int, input().split()):
    i = x - 1
    while i < n and (not lamps[i]):
        lamps[i] = x
        i += 1
print(*lamps)
