from itertools import product
with open(0) as f:
    (a, b, c, x) = map(int, f.read().split())
cnt = 0
for (i, j, k) in product(range(a + 1), range(b + 1), range(c + 1)):
    if 500 * i + 100 * j + 50 * k == x:
        cnt += 1
print(cnt)
