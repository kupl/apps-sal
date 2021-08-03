n, m, k = list(map(int, input().split()))
r = (k - 1) // (2 * m) + 1
d = ((k - 1) % (2 * m)) // 2 + 1
if k % 2 == 0:
    s = 'R'
else:
    s = 'L'
print(r, d, s)
