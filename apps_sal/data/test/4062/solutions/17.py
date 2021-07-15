a, b, c, d = map(int, input().split(' '))

l = []
l.append(a * c)
l.append(a * d)
l.append(b * c)
l.append(b * d)
print(max(l))
