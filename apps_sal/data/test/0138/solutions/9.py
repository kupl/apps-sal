n, a, b, c = [int(x) for x in input().split()]

min_sum = 10 * (a + b + c)

for i in range(4):
    for j in range(4):
        for k in range(4):
            if (n + 1 * i + 2 * j + 3 * k) % 4 == 0:
                min_sum = min(min_sum, i * a + j * b + k * c)

print(min_sum)
