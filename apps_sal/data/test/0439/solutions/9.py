y = int(input())
x = int(input())

if y > 30:
    print(x)
else:
    z = 1
    for i in range(y):
        z *= 2
    print(x % z)
