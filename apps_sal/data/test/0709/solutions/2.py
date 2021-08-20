n = int(input())
a = 0
while n > 0:
    a += n % 2
    n //= 2
print(a)
