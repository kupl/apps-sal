from itertools import permutations
(t, r) = ([0, 1, 4, 6, 5, 2], {i: 0 for i in '0123456789'})
for i in input():
    r[i] += 1
for i in '1689':
    r[i] -= 1
s = a = b = 0
for i in '9876543210':
    (a, b) = (b, (b + r[i]) % 6)
    s += int(i) * (t[b] - t[a])
d = pow(10, b, 7)
for q in permutations('1689'):
    q = ''.join(q)
    if (s + d * int(q)) % 7 == 0:
        print(q + ''.join((i * r[i] for i in '0123456789')))
        break
