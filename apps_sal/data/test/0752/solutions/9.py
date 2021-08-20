from collections import Counter
n = int(input())
a = Counter((input().strip() for _ in range(n)))
b = Counter((input().strip() for _ in range(n)))
for sz in ['M', 'L', 'XL', 'XXL', 'XXXL', 'S', 'XS', 'XXS', 'XXXS']:
    m = min(a[sz], b[sz])
    a[sz] -= m
    b[sz] -= m
ans = 0
for num_x in range(1, 4):
    old = a['X' * num_x + 'S'] + a['X' * num_x + 'L']
    new = b['X' * num_x + 'S'] + b['X' * num_x + 'L']
    assert old == new
    ans += old
old = a['M'] + a['S'] + a['L']
new = b['M'] + b['S'] + b['L']
assert old == new
ans += old
print(ans)
