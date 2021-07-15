def sumd(n):
    v = 0
    while n > 0:
        v += n % 10
        n //= 10
    return v

n, v = int(input()), -1
a, b = 0, n + 1
while a < b - 1:
    c = (a + b) // 2
    if c ** 2 <= n:
        a = c
    else:
        b = c
while a > 0 and n // a - a <= 81:
    if n % a == 0 and n // a - a == sumd(a):
        v = a
    a -= 1
print(v)

