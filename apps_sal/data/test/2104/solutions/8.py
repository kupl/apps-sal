(l, r) = map(int, input().split())
if r - l == 0:
    print('NO')
else:
    print('YES')
    for i in range(l, r + 1, 2):
        print(i, i + 1)
