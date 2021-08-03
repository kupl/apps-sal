n = int(input())
a = 0
while n >= 10:
    n += 1
    a += 1
    while n % 10 == 0:
        n = n // 10

print(a + 9)
