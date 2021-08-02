import math
t = int(input())
while t:
    t -= 1
    n = int(input())
    temp = math.ceil(n / 4)
    s = '9' * (n - temp) + '8' * temp
    print(s)
