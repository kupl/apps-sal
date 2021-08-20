(i, m) = (input, 998244353)
i()
a = map(int, i().split())
(r, c) = [next(a)] * 2
for j in a:
    (r, c) = ((2 * r + c + j) % m, (2 * c + j) % m)
print(r)
