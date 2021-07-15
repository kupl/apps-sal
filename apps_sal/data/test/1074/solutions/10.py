n = int(input())
a = 0
while n:
    if n % 8 == 1:
        a += 1
    n //= 8

print(a)
