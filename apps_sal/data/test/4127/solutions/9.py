import math
l = input().split(" ")
a = int(l[0])

b = (l[1].split("."))
c = int(b[0])
d = int(b[1])

e = a*(c*100 + d)//100
print(e)
