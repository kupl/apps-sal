a = input()
b = input()
h1 = int(a[0:2])
m1 = int(a[3:])
h2 = int(b[0:2])
m2 = int(b[3:])
h1 = h1 * 60 + m1
h2 = h2 * 60 + m2
h = (h1 + h2) // 2
h1 = h // 60
m1 = h - h1 * 60
print('0' * (2 - len(str(h1))) + str(h1) + ':' + '0' * (2 - len(str(m1))) + str(m1))
