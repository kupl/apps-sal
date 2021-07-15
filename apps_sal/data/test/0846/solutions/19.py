lamp, step = map(int, input().split())
steps = list(map(int, input().split()))
lamps = []
for i in range(lamp):
    lamps.append(i + 1)
for i in range(lamp):
    j = 0
    while steps[j] > lamps[i]:
        j += 1
    lamps[i] = steps[j]
print(' '.join(map(str, lamps)))
