m, n = [int(x) for x in input().split()]
print(sum(x * (pow(x / m, n) - pow((x - 1) / m, n)) for x in range(1, m + 1)))

