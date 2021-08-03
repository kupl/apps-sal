n = int(input())
if n % 2 == 0:
    print(int(n**2 / 2))
    for cont in range(0, n, 2):
        s = 'C.' * int(n / 2)
        print(s)
        s = '.C' * int(n / 2)
        print(s)
else:
    print(int((n**2 + 1) / 2))
    print('C.' * int(n / 2) + 'C')
    for cont in range(1, n, 2):
        print('.C' * int(n / 2) + '.')
        print('C.' * int(n / 2) + 'C')
