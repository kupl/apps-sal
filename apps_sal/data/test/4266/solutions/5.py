a, b = map(int, input().split())
c = []
x = 1
c.append(b - a + 1)
for i in range((abs(a) - 1) * 2):
    c.append(c[0] + x)
    x += 1
c = [str(n) for n in c]
c = ' '.join(c)
print(c)
