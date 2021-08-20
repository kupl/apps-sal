(n, m) = map(int, input().split())
clicks = list(map(int, input().split()))
lamps = [-1] * (n + 1)
pointer = n + 1
for i in range(m):
    for j in range(clicks[i], pointer):
        lamps[j] = clicks[i]
    pointer = min(pointer, clicks[i])
lamps = lamps[1:]
print(*lamps)
