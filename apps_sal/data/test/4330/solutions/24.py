(a, b) = list(map(int, input().split()))
if a == b:
    print(0)
elif (a + b) % 2 == 0:
    print((a + b) // 2)
else:
    print('IMPOSSIBLE')
