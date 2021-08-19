(n, a, b) = map(int, input().split())
if n * a < b:
    x = n * a
else:
    x = b
print(x)
