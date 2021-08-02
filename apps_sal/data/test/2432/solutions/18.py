a = bin(int(input()))[2:]
a = '0' * (6 - len(a)) + a
a = list(a)
a[0], a[1], a[2], a[3], a[4], a[5] = a[0], a[5], a[3], a[2], a[4], a[1]
print(int(''.join(a), 2))
