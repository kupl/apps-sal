n = int(input())
if n == 1:
    print('0 1')
elif n == 2:
    print('0 2')
else:
    d = n - 5
    minDay = ((d // 7) * 2) + (2 if d % 7 >= 2 else d % 7)
    maxDay = ((n // 7) * 2) + (2 if n % 7 >= 2 else n % 7)
    print('%d %d' % (minDay, maxDay))

