(h1, m1) = list(map(int, input().split(':')))
(h2, m2) = list(map(int, input().split(':')))
if m2 > m1:
    m1 += 60
    h1 -= 1
h1 -= h2
m1 -= m2
if h1 < 0:
    h1 += 24
h = ''
m = ''
if h1 < 10:
    h = '0'
h += str(h1)
if m1 < 10:
    m = '0'
m += str(m1)
print(h, m, sep=':', end='\n')
