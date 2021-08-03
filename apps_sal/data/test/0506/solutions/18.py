a, b = (list(map(int, input().split())))
count = 0

while ((b != 0) and (a != 0)):
    if b > a:
        count = count + b // a
        b = b % a
        a = a
    elif b < a:
        count = count + a // b
        b = b
        a = a % b


print(count)
