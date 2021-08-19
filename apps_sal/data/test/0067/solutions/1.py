(x, y, z) = map(int, input().split())
best = x - y + z
worst = x - y - z
if worst > 0:
    print('+')
elif best < 0:
    print('-')
elif worst == 0 and best == 0:
    print('0')
else:
    print('?')
