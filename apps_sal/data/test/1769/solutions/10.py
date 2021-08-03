a = int(input())
b = int(input())
print(b + 1, end=' ')
x = b
for i in range(b):
    print(x, end=' ')
    x -= 1
x = b + 2
for i in range(a):
    print(x, end=' ')
    x += 1
