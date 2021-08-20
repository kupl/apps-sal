(a1, a2, a3) = [int(x) for x in input().split(' ')]
(b1, b2, b3) = [int(x) for x in input().split(' ')]
n = int(input())
at = (a1 + a2 + a3) // 5
ar = (a1 + a2 + a3) % 5
bt = (b1 + b2 + b3) // 10
br = (b1 + b2 + b3) % 10
if ar > 0:
    at = at + 1
if br > 0:
    bt = bt + 1
if at + bt <= n:
    print('YES')
else:
    print('NO')
