(a, b) = map(int, input().split())
c = []
c.append(a + b)
c.append(a - b)
c.append(a * b)
c = sorted(c, reverse=True)
print(c[0])
