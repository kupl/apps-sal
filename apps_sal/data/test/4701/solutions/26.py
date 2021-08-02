n, k = int(input()), int(input()); a = 1
while a <= k:
    if n == 0:
        print(a)
        return
    a *= 2
    n -= 1
while n > 0:
    a += k
    n -= 1
print(a)
