(a, b, c) = map(int, input().split())
if c == 0 and b == a or (c != 0 and (b - a) % c == 0 and ((b - a) // c >= 0)):
    print('YES')
else:
    print('NO')
