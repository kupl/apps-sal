n = int(input(""))
a = []
b = []
for i in range(n):
    cc = input("").split(" ")
    a += [int(cc[0])]
    b += [int(cc[1])]
s = 0
a.sort()
b.sort()
if (n % 2 == 0):
    s = (a[int(n / 2)] + a[int(n / 2) - 1] - b[int(n / 2)] - b[int(n / 2) - 1])
else:
    s = a[int((n - 1) / 2)] - b[int((n - 1) / 2)]
print((int(-s + 1)))
