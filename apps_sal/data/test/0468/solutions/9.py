from math import log
x, y = list(map(int, input().split()))


xx, yy = (log(x) / x), (log(y) / y)

if(xx > yy):
    print(">")
elif (xx < yy):
    print("<")
else:
    print("=")
