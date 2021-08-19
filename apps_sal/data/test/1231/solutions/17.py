(i, j) = list(map(int, input().split()))
if not i and (not j):
    print('NO')
elif abs(i - j) > 1:
    print('NO')
else:
    print('YES')
