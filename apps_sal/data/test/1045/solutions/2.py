(n, i) = (int(input()), 0)
while n * 2 >= i * (i + 1):
    n -= i * (i + 1) // 2
    i += 1
print(i - 1)
