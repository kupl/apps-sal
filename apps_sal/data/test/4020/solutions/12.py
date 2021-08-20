(h1, m1) = list(map(int, input().split(':')))
(h2, m2) = list(map(int, input().split(':')))
total1 = h1 * 60 + m1
total2 = h2 * 60 + m2
moy = (total1 + total2) // 2
h3 = moy // 60
m3 = moy % 60
if h3 < 10:
    h3 = '0' + str(h3)
if m3 < 10:
    m3 = '0' + str(m3)
print('{}:{}'.format(h3, m3))
