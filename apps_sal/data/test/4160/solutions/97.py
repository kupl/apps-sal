X = int(input()); n = 100; a = 0
while n < X:
    a += 1
    n += n // 100
print(a)
