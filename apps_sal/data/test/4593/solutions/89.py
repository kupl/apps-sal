x = int(input())
mx = 0
for b in range(1, int(1000 ** 0.5) + 1):
    for p in range(2, 10):
        if mx < b ** p <= x:
            mx = b ** p
print(mx)
