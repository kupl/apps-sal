n = int(input())

# 0 1 3 6 7 9 12 13 15 18 19 21 24 ...
if n % 3 == 0:
    print('yes')
elif n % 6 == 0:
    print('yes')
elif n % 6 == 1:
    print('yes')
elif n == 0 or n == 1:
    print('yes')
else:
    print('no')
