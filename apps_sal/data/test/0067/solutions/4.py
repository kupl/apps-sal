x, y, z = list(map(int, input().split()))

total = x - y

if total - z > 0:
    print('+')
elif total + z < 0:
    print('-')
elif z == 0 and total == 0:
    print('0')
else:
    print('?')
