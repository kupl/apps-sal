(h1, m1) = list(map(int, input().split(':')))
(h2, m2) = list(map(int, input().split(':')))
minutes = h2 * 60 - h1 * 60 + m2 - m1
minutes //= 2
h1 = h1 + (m1 + minutes) // 60
m1 = (m1 + minutes) % 60
h1 = str(h1)
h1 = '0' * (2 - len(h1)) + h1
m1 = str(m1)
m1 = '0' * (2 - len(m1)) + m1
print(h1 + ':' + m1)
