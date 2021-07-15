a, b, c = map(int, input().split())

temp = c
c = b
b = a
a = temp
print(a, b, c)
