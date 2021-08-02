a = input().split()
if a[2] == 'month':
    print(12 - (int(a[0]) >= 30) - 4 * (int(a[0]) == 31))
else:
    print(53 if int(a[0]) in (5, 6) else 52)
