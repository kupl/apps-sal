(n, m) = map(int, input().split())
for i in range(n):
    s = input().strip()
    for j in range(m):
        if s[j] == '.':
            if i % 2 == 0:
                if j % 2 == 0:
                    print('B', end='')
                else:
                    print('W', end='')
            elif j % 2 == 0:
                print('W', end='')
            else:
                print('B', end='')
        else:
            print('-', end='')
    print('')
