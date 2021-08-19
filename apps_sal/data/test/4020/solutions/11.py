def mp():
    return map(int, input().split(':'))


(h1, m1) = mp()
(h2, m2) = mp()
r = h1 * 60 + m1 + h2 * 60 + m2
r = r // 2
h3 = str(r // 60)
if len(h3) == 1:
    h3 = '0' + h3
m3 = str(r % 60)
if len(m3) == 1:
    m3 = '0' + m3
print(h3, ':', m3, sep='')
