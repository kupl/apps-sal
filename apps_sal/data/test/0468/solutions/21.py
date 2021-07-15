from math import log
x, y = [int(x) for x in input().split()]
if y*log(x) == x*log(y):
    print("=")
elif y*log(x) < x*log(y):
    print("<")
else:
    print(">")

