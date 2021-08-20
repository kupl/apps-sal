(n, m) = list(map(int, input().split()))
a = 1
for i in range(n):
    if a == 1:
        print('0', end='')
    else:
        print('1', end='')
    a *= -1
