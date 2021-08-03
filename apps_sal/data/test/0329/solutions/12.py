x = input()
a = x.count('n')
b = x.count('i')
c = x.count('e')
d = x.count('t')
if a >= 5:
    a -= 1
    a /= 2
else:
    a /= 3
c /= 3
a = int(a)
c = int(c)
i = 0
while a > 0 and b > 0 and c > 0 and d > 0:
    i += 1
    a -= 1
    b -= 1
    c -= 1
    d -= 1
print(i)

# 1481311408782
