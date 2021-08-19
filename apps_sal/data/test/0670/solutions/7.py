import math
s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
s = input().split()
x1 = int(s[0])
y1 = int(s[1])
x2 = int(s[2])
y2 = int(s[3])
if x1 == x2:
    print(abs(y1 - y2))
elif y1 == y2:
    print(abs(x1 - x2))
elif a != 0 and b != 0:
    var1 = abs(x1 - x2) + abs(y1 - y2)
    var2 = 0
    x = x1
    y = (a * x + c) / b * -1
    var2 += abs(y1 - y)
    x3 = x2
    y3 = (a * x3 + c) / b * -1
    var2 += math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
    var2 += abs(y3 - y2)
    var3 = 0
    x = x1
    y = (a * x + c) / b * -1
    var3 += abs(y1 - y)
    y3 = y2
    x3 = (b * y3 + c) / a * -1
    var3 += math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
    var3 += abs(x3 - x2)
    var4 = 0
    y = y1
    x = (b * y + c) / a * -1
    var4 += abs(x1 - x)
    y3 = y2
    x3 = (b * y3 + c) / a * -1
    var4 += math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
    var4 += abs(x3 - x2)
    var5 = 0
    y = y1
    x = (b * y + c) / a * -1
    var5 += abs(x1 - x)
    x3 = x2
    y3 = (a * x3 + c) / b * -1
    var5 += math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
    var5 += abs(y3 - y2)
    print(min(var1, var2, var3, var4, var5))
else:
    print(abs(x1 - x2) + abs(y1 - y2))
