a = list(input())
b = list(input())
c = list(input())
t = a.pop(0)
l = 0
while True:
    if t == 'a':
        if len(a) == 0:
            break
        t = a.pop(0)
    elif t == 'b':
        if len(b) == 0:
            break
        t = b.pop(0)
    elif t == 'c':
        if len(c) == 0:
            break
        t = c.pop(0)
print(t.upper())
