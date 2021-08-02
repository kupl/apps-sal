n, a, b, c = map(int, input().split())
m = 10**12
for i in range(30):
    for j in range(30):
        for k in range(30):
            if (n + i + 2 * j + 3 * k) % 4:
                continue
            m = min(m, i * a + j * b + k * c)
print(m)
