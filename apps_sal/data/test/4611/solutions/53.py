n = int(input())
bt = 0
bx = 0
by = 0
for _ in range(n):
    (t, x, y) = map(int, input().split())
    dt = abs(x - bx) + abs(y - by)
    if dt > t - bt or dt % 2 != (t - bt) % 2:
        print('No')
        break
    bt = t
    bx = x
    by = y
else:
    print('Yes')
