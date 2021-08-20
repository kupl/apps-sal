n = int(input())
if n == 1:
    print('1')
    print('1')
elif n == 2:
    print('1')
    print('1')
elif n == 3:
    print('2')
    print('1 3')
elif n == 4:
    print('4')
    print('3 1 4 2')
else:
    print(n)
    l = []
    m = 0
    for i in range(1, (n + 1) // 2 + 1):
        l.append(str(i))
        m = i
    for i in range(n // 2):
        l.insert(2 * i + 1, str(m + i + 1))
    print(' '.join(l))
