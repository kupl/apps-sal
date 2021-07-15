n = int(input())

x = n % 10

if x == 3:
    print('bon')
elif x == 0 or x == 1 or x == 6 or x == 8:
    print('pon')
else:
    print('hon')

