(a, b, c) = map(int, input().split())
if c and (not (a - b) % c) and (max(a + c, b) - min(b, a + c) < max(a, b) - min(a, b)) or a == b:
    print('YES')
else:
    print('NO')
