(a, b, c) = map(int, input().split())
if a + b + c == 17 and (a == 5 or a == 7) and (b == 5 or b == 7) and (c == 5 or c == 7):
    print('YES')
else:
    print('NO')
