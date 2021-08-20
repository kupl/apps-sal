(a, b) = input().split()
a = int(a)
b = int(b)
if (a + b) % 3 == 0:
    print('Possible')
elif a % 3 == 0:
    print('Possible')
elif b % 3 == 0:
    print('Possible')
else:
    print('Impossible')
