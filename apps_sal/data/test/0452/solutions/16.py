(p, q) = [int(x) for x in input().split()]
n = int(input())
a = [int(x) for x in input().split()]
(x, y) = (1, 0)
for i in a[::-1]:
    (x, y) = (y + i * x, x)
if x * q == y * p:
    print('YES')
else:
    print('NO')
