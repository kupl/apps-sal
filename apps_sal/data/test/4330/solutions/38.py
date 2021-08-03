A, B = map(int, input().split())
K = A + B
if K % 2:
    print('IMPOSSIBLE')
else:
    print(K // 2)
