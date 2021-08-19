(p, t) = ({}, input())
for i in '0123456789':
    p[i] = 0
for i in t:
    p[i] += 1
for i in '1689':
    p[i] -= 1
q = [0] * 7
r = pow(10, (len(t) - 4) % 6, 7)
for (i, j) in enumerate([9681, 6819, 6981, 6891, 8691, 9861, 1896]):
    q[i * r % 7] = j
s = [0] + [int('1' * i) % 7 for i in range(1, 6)]
a = b = d = 0
for i in '0123456789':
    b = (a + p[i]) % 6
    d -= (s[b] - s[a]) * int(i) % 7
    a = b
print(str(q[d % 7]) + ''.join((i * p[i] for i in '9876543210')))
