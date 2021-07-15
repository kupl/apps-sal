n = int(input())
for i in range(n):
    if i % 4 < 2:
        print('a', end='')
    else:
        print('b', end='')
