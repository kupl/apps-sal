(a, b, c, d) = list(map(int, input().split()))
(x, y) = list(map(int, input().split()))
if abs(c - a) % abs(x) == 0 and abs(c - a) / abs(x) % 2 == abs(d - b) / abs(y) % 2 and (abs(d - b) % abs(y) == 0):
    print('YES')
else:
    print('NO')
