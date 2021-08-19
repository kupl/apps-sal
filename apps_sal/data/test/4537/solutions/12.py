(a, b) = input().split()
a = int(a)
b = int(b)
ls = [a + b, a - b, a * b]
ls.sort()
print(ls[2])
