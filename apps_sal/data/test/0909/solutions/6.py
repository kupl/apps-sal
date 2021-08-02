__author__ = 'hamed1soleimani'

a = int(input())
b = int(input())
c = int(input())

out = list()
out.append(a + (b * c))
out.append((a * b) + c)
out.append(a + b + c)
out.append(a * b * c)
out.append(a * (b + c))
out.append((a + b) * c)

print(max(out))
