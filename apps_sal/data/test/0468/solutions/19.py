from math import log
x, y = list(map(int, input().split()))
a = y * log(x)
b = x * log(y)
if a < b: print("<")
elif a == b: print("=")
else: print(">")

