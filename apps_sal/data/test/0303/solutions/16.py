inp = list(map(int, input().split()))
(x1, y1, x2, y2) = [inp[i] for i in range(4)]
inp = list(map(int, input().split()))
(x, y) = (inp[0], inp[1])
d1 = x2 - x1
d2 = y2 - y1
if d1 % x == 0 and (int(d1 / x) + int(d2 / y)) % 2 == 0 and (d2 % y == 0):
    print('YES')
else:
    print('NO')
