a, b = list(map(int, input().split()))
if a == b == 0:
    print('NO')
else:
    print('YES' if abs(a - b) <= 1 else 'NO')
