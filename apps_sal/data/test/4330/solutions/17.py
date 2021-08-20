(a, b) = list(map(int, input().split()))
s = a + b
if s % 2 == 1:
    print('IMPOSSIBLE')
else:
    print(s // 2)
