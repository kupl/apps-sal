a = input()
b = a.split()
d = int(b[0])
n = int(b[1])
if n == 100:
    print(((100**d) * (n + 1)))
else:
    print(((100**d) * n))
