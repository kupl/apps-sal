(a, b) = [int(i) for i in input().split()]
if (a + b) % 2 == 0:
    print(int(abs(a + b) / 2))
else:
    print('IMPOSSIBLE')
