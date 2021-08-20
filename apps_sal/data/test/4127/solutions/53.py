(a, b) = input().split()
(c, d) = b.split('.')
e = int(c) * 100 + int(d)
f = int(a) * e
print(f // 100)
