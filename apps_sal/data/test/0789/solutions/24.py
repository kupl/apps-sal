n = int(input())
a = ''
while n != 0:
    if n % 10 == 4:
        a = '0' + a
    elif n % 10 == 7:
        a = '1' + a
    n = n // 10
a = '1' + a
m = int(a, 2)
m = m - 1
print(m)
