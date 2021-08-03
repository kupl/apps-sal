a = int(input())
c = 0
while a > 0:
    if a % 10 < 9 and a > 9:
        t = 10 + a % 10
    else:
        t = a % 10
    c += t
    a -= t
    a //= 10
print(c)
