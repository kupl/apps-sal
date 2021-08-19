(l, r, x, y, k) = map(int, input().split())
L = x - 1
R = y + 1
while R - L > 1:
    M = (L + R) // 2
    if M * k <= r:
        L = M
    else:
        R = M
if L * k >= l and L != x - 1:
    print('YES')
else:
    print('NO')
