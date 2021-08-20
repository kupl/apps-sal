(n, m, k) = map(int, input().split())
per1 = (k - 1) // (2 * m)
print(1 + per1, end=' ')
per2 = k - per1 * (2 * m)
print(1 + (per2 - 1) // 2, end=' ')
if k % 2 == 0:
    print('R')
else:
    print('L')
