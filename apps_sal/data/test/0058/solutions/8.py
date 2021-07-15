n = int(input())
a = int(input())
b = int(input())

result = 6
if 4 * a + 2 * b <= n:
    result = min(1, result)
if 2 * a + b <= n:
    result = min(2, result)
if 4 * a <= n:
    result = min(3, result)
if 2 * b <= n:
    if a + 2 * b <= n:
        if n // a >= 3:
            result = min(2, result)
        elif n // a == 2:
            result = min(3, result)
        else:
            result = min(4, result)
    else:
        if n // a >= 4:
            result = min(2, result)
        elif n // a == 3:
            result = min(3, result)
        elif n // a == 2:
            result = min(4, result)
        else:
            result = min(5, result)
if a + b <= n:
    if 2 * a <= n:
        result = min(3, result)
    else:
        result = min(4, result)
if 2 * a <= n:
    result = min(4, result)
print(result)



