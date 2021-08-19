n = int(input())
s = ''
if n % 4 == 0:
    print(0)
    s += str(n // 2) + ' '
    for i in range(n // 4):
        s += str(4 * i + 1) + ' '
        s += str(4 * i + 4) + ' '
    print(s[:-1])
elif n % 4 == 3:
    print(0)
    s += str(n // 2 + 1) + ' '
    s += '1 2 '
    for i in range(n // 4):
        s += str(4 * i + 4) + ' '
        s += str(4 * i + 7) + ' '
    print(s[:-1])
elif n % 4 == 2:
    print(1)
    s += str(n // 2) + ' 1 '
    for i in range(0, n // 4):
        s += str(4 * i + 3) + ' '
        s += str(4 * i + 6) + ' '
    print(s[:-1])
else:
    print(1)
    s += str(n // 2 + 1) + ' 1 '
    for i in range(0, n // 4):
        s += str(4 * i + 2) + ' '
        s += str(4 * i + 5) + ' '
    print(s[:-1])
