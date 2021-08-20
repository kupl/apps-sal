(n, a, b) = input().split()
n = int(n)
a = int(a)
b = int(b)
potatos = 0
counter = 0
customers = input().split()
for i in customers:
    if i == '1':
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
            potatos += 1
        elif potatos > 0:
            potatos -= 1
        else:
            counter += 1
    elif b > 0:
        b -= 1
    else:
        counter += 2
print(counter)
