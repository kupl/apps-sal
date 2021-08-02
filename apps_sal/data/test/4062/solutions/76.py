x, y, z, w = map(int, input().split())
l = []
l.append(x * z)
l.append(x * w)
l.append(y * z)
l.append(y * w)
print(max(l))
