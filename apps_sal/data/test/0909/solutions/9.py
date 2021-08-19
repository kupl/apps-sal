a = int(input())
b = int(input())
c = int(input())
result = 0
if a != 1:
    if b != 1:
        if c != 1:
            result = a * b * c
        else:
            result = a * (b + 1)
    elif c != 1:
        result = max([a, c]) * (min([a, c]) + 1)
    else:
        result = 2 * a
elif b == 1:
    if c != 1:
        result = 2 * c
    else:
        result = 3
elif c == 1:
    result = b + 2
else:
    result = (1 + b) * c
print(result)
