(n, k) = map(int, input().split())
a = (n - k + 2) * ((k + n + 1) * (n + 1) + 2) // 2
b = (n + 1) * (n + 2) * (2 * n + 3) // 6
c = (k - 1) * k * (2 * k - 1) // 6
print((a - b + c) % (10 ** 9 + 7))
