
a, b = list(map(str, input().split()))

a = int(a)
b = int(b[0] + b[2:])
print((a * b // 100))
