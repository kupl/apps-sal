a, b = [input() for i in range(2)]
c = a[::-1]
d = b[::-1]

if a == d and b == c:
    print('YES')

else:
    print('NO')
