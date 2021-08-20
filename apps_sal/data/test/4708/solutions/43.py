(n, k, x, y) = [int(input()) for i in range(4)]
print(n * x + min(0, (k - n) * (x - y)))
