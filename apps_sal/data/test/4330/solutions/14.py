(a, b) = map(int, input().split())
k = (a + b) // 2
if a + b == 2 * k:
    print(k)
else:
    print('IMPOSSIBLE')
