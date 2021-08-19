(n, k1, k2) = input().split()
a = input().split()
b = input().split()
c = [abs(int(a[i]) - int(b[i])) for i in range(int(n))]
for i in range(int(k1) + int(k2)):
    c.sort()
    c[int(n) - 1] = abs(c[int(n) - 1] - 1)
e = 0
for i in range(int(n)):
    e += c[i] ** 2
print(e)
