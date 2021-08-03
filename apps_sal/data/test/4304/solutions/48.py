a, b = map(int, input().split())

n = b - a - 1

x = (n**2 + n - a * 2) // 2

print(x)
