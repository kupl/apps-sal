n = int(input())
if n == 0 or n == 1:
    print('yes')
elif n % 3 == 0:
    print('yes')
elif n % 6 == 1:
    print('yes')
else:
    print('no')
