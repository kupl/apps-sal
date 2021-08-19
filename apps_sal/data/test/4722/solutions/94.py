(a, b) = map(int, input().split())
total = a + b
if total % 3 == 0:
    print('Possible')
elif a % 3 == 0:
    print('Possible')
elif b % 3 == 0:
    print('Possible')
else:
    print('Impossible')
