n = int(input())
a = (n >> 5) & 1
b = (n >> 4) & 1
c = (n >> 3) & 1
d = (n >> 2) & 1
e = (n >> 1) & 1
f = n & 1
print(((((a*2+f)*2+d)*2+c)*2+e)*2+b)

