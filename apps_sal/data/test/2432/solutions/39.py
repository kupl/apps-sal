a = int(input())
a = bin(a)[2:]
a = "0" * (6 - len(a)) + a
p = [0, 5, 3, 2, 4, 1]
b = ['-'] * 6
for i in range(6):
  b[i] = a[p[i]]
b = "".join(b)
print(int(b, 2))

