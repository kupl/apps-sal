h1, m1 = tuple(map(int, input().split(':')))
h2, m2 = tuple(map(int, input().split(':')))


sered = ((h2 * 60 + m2) - (h1 * 60 + m1)) // 2 + (h1 * 60 + m1)

h = str(sered // 60)
m = str(sered % 60)

if len(h) == 1:
    h = '0' + h
if len(m) == 1:
    m = '0' + m
print(h, m, sep=':')

