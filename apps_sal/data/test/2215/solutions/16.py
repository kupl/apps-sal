(n, m) = map(int, input().split(' '))
l = []
r = []
for i in range(m):
    (l_i, r_i) = map(int, input().split(' '))
    l.append(l_i)
    r.append(r_i)
s = ''
for i in range(n):
    if i % 2 == 0:
        s += '0'
    else:
        s += '1'
print(s)
