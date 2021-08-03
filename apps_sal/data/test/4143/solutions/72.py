n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

aa = -(-n // a)
bb = -(-n // b)
cc = -(-n // c)
dd = -(-n // d)
ee = -(-n // e)

print(max(aa, bb, cc, dd, ee) + 4)
