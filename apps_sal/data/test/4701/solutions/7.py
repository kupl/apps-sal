a = int(input())
b = int(input())
c = 1
for i in range(a):
    if 2 * c <= c + b:
        c = 2 * c
    else:
        c = c + b
print(c)
