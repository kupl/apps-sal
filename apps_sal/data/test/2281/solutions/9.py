n = int(input())
if n % 2 == 0:
    a = []
    for i in range(1, n, 2):
        a.append(i)
    a = a + a[::-1]
    b = []
    for i in range(2, n, 2):
        b.append(i)
    a = a + [n] + b + [n] + b[::-1]
    print(*a)
else:
    a = []
    for i in range(1, n, 2):
        a.append(i)
    a = a + [n] + a[::-1] + [n]
    b = []
    for i in range(2, n, 2):
        b.append(i)
    a = a + b + b[::-1]
    print(*a)
