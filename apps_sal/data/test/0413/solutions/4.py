import math
t = input()
loc = t.split(' ')
n = int(loc[0])
m = int(loc[1])
b = math.ceil(math.log2(m / n))
c = 0
temp = m
if m <= n:
    d = n - m
else:
    for i in range(1, b + 1):
        if temp % 2 == 0:
            temp = temp / 2
        else:
            c = c + 1
            temp = (temp + 1) / 2
    d = c + n - temp + b
print(int(d))
