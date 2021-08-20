n = int(input())
if n % 6 == 0 or (n - 1) % 6 == 0 or (n - 3) % 6 == 0:
    print('yes')
else:
    print('no')
