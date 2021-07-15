h1, m1 = list(map(int, input().split(':')))
h2, m2 = list(map(int, input().split(':')))

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

delta = (t2 - t1) // 2
t1_f = t1 + delta
h1_f = t1_f // 60
m1_f = t1_f % 60
print('{:02d}:{:02d}'.format(h1_f, m1_f))

