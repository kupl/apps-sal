(n, m, k) = map(int, input().split())
pl = ''
if k % 2 == 0:
    pl = 'R'
else:
    pl = 'L'
k = k // 2 + k % 2
part = k % m
rad = k // m + 1
if k % m == 0:
    rad -= 1
if part == 0:
    part = m
print(rad, part, pl)
