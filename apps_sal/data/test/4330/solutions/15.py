(a, b) = list(map(int, input().split()))
if a == -b:
    print('IMPOSSIBLE')
elif (a + b) // 2 != (a + b) / 2:
    print('IMPOSSIBLE')
else:
    print((a + b) // 2)
