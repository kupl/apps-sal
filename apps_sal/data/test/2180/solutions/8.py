n = int(input())
if n % 2 == 0:
    print(n**2 // 2)
else:
    print(n ** 2 // 2 + 1)
d = [['.'] * n for i in range(n)]
for i in range(n):
    if i % 2 != 0:
        print('.C' * (n // 2) + '.' * (n % 2))
    else:
        print('C.' * (n // 2) + 'C' * (n % 2))
