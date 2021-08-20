(n, d) = list(map(int, input().split()))
if n // (2 * d + 1) == n / (2 * d + 1):
    print(n // (2 * d + 1))
else:
    print(n // (2 * d + 1) + 1)
