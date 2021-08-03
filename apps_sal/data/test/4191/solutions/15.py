a = int(input())
b = int(input())
c = int(input())
d = int(input())
# print(a,b,c,d)
x1 = a ^ b
x2 = c | d
x3 = b & c
x4 = a ^ d

x5 = x1 & x2
x6 = x3 | x4
print(x5 ^ x6)
