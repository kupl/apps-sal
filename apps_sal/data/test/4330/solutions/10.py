a, b = map(int, input().split())
if a % 2 == 0 and b % 2 == 1:
    print('IMPOSSIBLE')
elif a % 2 == 1 and b % 2 == 0:
    print('IMPOSSIBLE')
else:
    print((a + b) // 2)
