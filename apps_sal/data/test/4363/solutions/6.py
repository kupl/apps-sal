K, S = map(int, input().split())
total = 0
count = 0

for x in range(0, K + 1):
    for y in range(0, K + 1):
        if K >= (S - x - y) and (S - x - y) >= 0:
            count += 1
print(count)
