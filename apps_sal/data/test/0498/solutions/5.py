(n, m, k) = map(int, input().split())
pos = ''
if k % 2 == 0:
    pos = 'R'
else:
    pos = 'L'
rad = (k - 1) // (2 * m) + 1
parta = (k - (rad - 1) * 2 * m + 1) // 2
print(rad, parta, pos)
