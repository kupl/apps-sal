n = int(input())
(a, b) = map(int, input().split())
(b1, b2) = map(int, input().split())
(c1, c2) = map(int, input().split())
b1 -= a
b2 -= b
c1 -= a
c2 -= b
if b1 == 0 or b2 == 0 or c1 == 0 or (c2 == 0):
    print('NO')
elif b1 * c1 < 0 or b2 * c2 <= 0:
    print('NO')
else:
    print('YES')
