n = int(input())
a = n
c = 0
while a >= 10:
    a //= 10
    c += 1
b = a * 10 ** c - 1
a = n - b
c = 0
while a != 0:
    c += a % 10
    a //= 10
a = b
while a != 0:
    c += a % 10
    a //= 10
print(c)
