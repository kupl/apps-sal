n = int(input())

count = 0

for c in range(1, n + 1):
    for b in range(1, c + 1):
        if b >= c ^ b > c - b:
            count += 1

print(count)

