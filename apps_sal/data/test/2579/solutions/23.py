(l, r, x, y, k) = list(map(int, input().split()))
ans = 0
for i in range(x, y + 1):
    if i * k <= r and i * k >= l:
        if ans == 0:
            print('YES')
            ans = 1
if ans == 0:
    print('NO')
