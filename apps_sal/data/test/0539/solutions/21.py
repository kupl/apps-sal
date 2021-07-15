n = int(input())
counter = 0
for c in range(1, n + 1):
    for b in range(1, c + 1):
        if b >= c ^ b > c - b:
            counter += 1

print(counter)
