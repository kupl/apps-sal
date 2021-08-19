n = int(input())
if n % 2 == 0:
    print(n ** 2 // 2)
    for i in range(n // 2):
        print('C.' * (n // 2))
        print('.C' * (n // 2))
else:
    print((n // 2 + 1) ** 2 + (n // 2) ** 2)
    for i in range(n // 2):
        print('C.' * (n // 2) + 'C')
        print('.C' * (n // 2) + '.')
    print('C.' * (n // 2) + 'C')
