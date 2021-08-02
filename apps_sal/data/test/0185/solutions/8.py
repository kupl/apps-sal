n, k = [int(x) for x in input().split()]
print(min(n - k, k - 1) + 3 * n)
