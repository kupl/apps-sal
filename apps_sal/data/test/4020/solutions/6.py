(h1, m1) = map(int, input().split(':'))
(h2, m2) = map(int, input().split(':'))
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
diff = t2 - t1
t = t1 + diff // 2
h3 = t // 60
m3 = t % 60
print('{:02}:{:02}'.format(h3, m3))
