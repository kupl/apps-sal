(K, S) = map(int, input().split())
count = 0
for x in range(K + 1):
    for y in range(K + 1):
        if 0 <= S - x - y <= K:
            count += 1
print(count)
