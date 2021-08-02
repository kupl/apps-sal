n = int(input())
k = int(input())
x = int(input())
y = int(input())

print((min(k, n) * x + max(n - k, 0) * y))
