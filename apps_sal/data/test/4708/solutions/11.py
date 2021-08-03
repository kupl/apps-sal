n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(x * min(n, k) + y * max(n - k, 0))
