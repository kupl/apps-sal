n, l = list(map(int, input().split()))
apples = []
min_val = l

for i in range(1, n + 1):
    apples.append(l + i - 1)
    if abs(l + i - 1) < abs(min_val):
        min_val = (l + i - 1)
apples.remove(min_val)

print((sum(apples)))

