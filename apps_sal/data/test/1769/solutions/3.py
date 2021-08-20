a = int(input())
b = int(input())
tot = a + b + 1
x = b + 1
s = ''
for i in range(x, tot + 1):
    s += str(i)
    s += ' '
for I in range(b, 0, -1):
    s += str(I)
    s += ' '
print(s)
