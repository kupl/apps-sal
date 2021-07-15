n, k = map(int, input().split())
d = int((9 + 8 * (n + k)) ** 0.5)
x = (d - 3) // 2
print(n - x)
