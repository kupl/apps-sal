n = int(input())
m = n**(1 / 2.0)
if(m == int(m)):
    m = int(m)
else:
    m = int(m) + 1
a = m
b = m
while(a * b >= n):
    b = b - 1
b = b + 1
print((a + b) * 2)
