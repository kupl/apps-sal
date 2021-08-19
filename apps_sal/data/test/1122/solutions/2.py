(n, m) = list(map(int, input().split()))
if n % 2 == 1:
    for i in range(m):
        print('{} {}'.format(2 + i, n - i))
else:
    for i in range(m):
        if i % 2 == 0:
            print('{} {}'.format(int(n / 2 - i / 2), int(n / 2 + 1 + i / 2)))
        else:
            print('{} {}'.format(int(2 + i // 2), int(n - i // 2)))
