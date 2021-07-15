X = int(input())

a, mod = divmod(X, 500)
b = mod // 5

print((a * 1000 + b * 5))

