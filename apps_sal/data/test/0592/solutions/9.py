n = int(input())
print(4 * sum(x * ((n - x) // x) for x in range(2, n)))
