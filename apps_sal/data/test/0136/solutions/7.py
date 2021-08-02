def c(a, b):
    for x, y in zip(a, b):
        if x > y:
            return '>'
        elif x < y:
            return '<'
    return '='


a, b = input(), input()
if len(a) < len(b):
    a = '0' * (len(b) - len(a)) + a
elif len(a) > len(b):
    b = '0' * (len(a) - len(b)) + b
print(c(a, b))
