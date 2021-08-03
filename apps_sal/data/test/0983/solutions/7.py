s = input()
c = s.split(' ')
for i in range(4):
    c[i] = int(c[i])
s = input()
a = s.split(' ')
for i in range(c[0]):
    a[i] = int(a[i])
    a[i] = [(c[1]) * a[i], (c[2]) * a[i], (c[3]) * a[i]]
dp = [[0, 0, 0] for i in range(c[0])]
m1 = -1000000000000000001
m2 = -2000000000000000001
m3 = -3000000000000000001
for i in range(c[0]):
    m1 = max(m1, a[i][0])
    m2 = max(m2, m1 + a[i][1])
    m3 = max(m3, m2 + a[i][2])
print(m3)
