n = int(input().strip())
kosi = list(map(int, input().strip().split()))
mini = 400
for a in range(len(kosi)):
    for b in range(a, len(kosi)):
        first = sum(kosi[a:b])
        second = sum(kosi[:a]) + sum(kosi[b:])
        if abs(first - second) < mini:
            mini = abs(first - second)
print(mini)
