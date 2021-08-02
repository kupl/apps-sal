x = int(input())
a = int(input())
b = int(input())

x -= a
while x >= b:
    x -= b

print(x)
