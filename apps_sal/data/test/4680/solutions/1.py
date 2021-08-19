(a, b, c) = map(int, input().split())
b5 = 0
b7 = 0
if a == 5:
    b5 += 1
if a == 7:
    b7 += 1
if b == 5:
    b5 += 1
if b == 7:
    b7 += 1
if c == 5:
    b5 += 1
if c == 7:
    b7 += 1
if b5 == 2 and b7 == 1:
    print('YES')
else:
    print('NO')
