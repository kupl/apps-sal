x, y = list(map(int, input().split()))

from math import log

xx, yy = (log(x) / x), (log(y) / y)

if(xx > yy):
    print(">")
elif (xx < yy):
    print("<")
else:
    print("=")

