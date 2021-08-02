x = int(input())
a = int(input())
b = int(input())

x -= a
num = x // b
x -= num * b
print(x)
