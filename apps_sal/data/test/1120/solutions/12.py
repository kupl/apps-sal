(n, a) = (int(input()), 0)
while n:
    n -= int(max(str(n)))
    a += 1
print(a)
