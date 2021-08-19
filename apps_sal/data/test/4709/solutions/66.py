s = input()
(a, op, b) = s.split()
a = int(a)
b = int(b)
if op == '+':
    c = a + b
else:
    c = a - b
print(c)
