N = 8
a = [list(input()) for i in range(N)]
amin = N
bmin = N
for c in range(8):
    r = 0
    while r < N and a[r][c] == '.':
        r += 1
    if r < N and a[r][c] == 'W':
        amin = min(amin, r)
    r = N - 1
    while r >= 0 and a[r][c] == '.':
        r -= 1
    if r >= 0 and a[r][c] == 'B':
        bmin = min(bmin, N - 1 - r)
if amin <= bmin:
    print('A')
else:
    print('B')
