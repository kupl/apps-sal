a = bin(int(input()))[2:]
a = (6 - len(a)) * '0' + a
b = a[0] + a[5] + a[3] + a[2] + a[4] + a[1]
print(int(b, 2))
