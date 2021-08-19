n = int(input().strip())
total = 0
for c in range(1, n + 1):
    for b in range((c + 1) // 2, c):
        a = c ^ b
        if a < b and a <= n and (a + b > c):
            total += 1
print(total)
