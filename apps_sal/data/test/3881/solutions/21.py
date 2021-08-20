from itertools import product
(n, q) = map(int, input().split())
ops = dict()
for _ in range(q):
    (a, b) = input().split()
    ops[a] = b
count = 0
for t in product('abcdef', repeat=n):
    s = ''.join(t)
    while len(s) > 1:
        s = ops.get(s[:2], 'g') + s[2:]
    count += s == 'a'
print(count)
