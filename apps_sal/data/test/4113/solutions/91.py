n = int(input())

if n >= 18:
    print('Yes')
elif n % 4 == 0 or n % 7 == 0:
    print('Yes')
elif n - 7 >= 0 and (n - 7) % 4 == 0:
    print('Yes')
else:
    print('No')
