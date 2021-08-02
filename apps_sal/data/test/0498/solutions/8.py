r, p, n = map(int, input().split())
print((n - 1) // (p * 2) + 1, (n - 1) % (p * 2) // 2 + 1, sep=' ', end=' ')
if n % 2 == 0:
    print('R')
else:
    print('L')
