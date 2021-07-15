a = list(str(input()))
b = list(str(input()))
c = list(str(input()))
n = a.pop(0)
m = 0
while True:
    if n == 'a':
        if len(a) == 0:
            break
        n = a.pop(0)
    elif n == 'b':
        if len(b) == 0:
            break
        n = b.pop(0)
    else:
        if len(c) == 0:
            break
        n = c.pop(0)
print(n.upper())
