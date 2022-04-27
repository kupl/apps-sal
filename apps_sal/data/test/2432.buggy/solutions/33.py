n = int(input())
a = list(bin(n)[2:])
a = ['0'] * (6 - len(a)) + a
(a[1], a[5]) = (a[5], a[1])
(a[2], a[3]) = (a[3], a[2])
print(int(''.join(a), 2))
