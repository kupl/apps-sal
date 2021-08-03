n = int(input())
print('YNEOS'[n != 12 and (n // 10 in (1, 2, 7, 9) or n % 10 in (1, 7, 9))::2])
