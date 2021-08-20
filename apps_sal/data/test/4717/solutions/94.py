(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
if abs(b - a) > abs(c - a):
    print('B')
else:
    print('A')
