n, m = map(int, input().split())

full_n = n // 5
full_m = m // 5

print(full_n * full_m * 5 + full_n * (m%5) + full_m * (n%5) + sum(1 for x in range(0, n % 5 + 1) for y in range(0, m % 5 + 1) if (x + y) % 5 == 0) - 1)
