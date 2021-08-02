a = input()
b = input()
s = input()

d = dict(zip(a, b))

for c in s:
    if c.lower() in d:
        if c.islower():
            print(d[c], end='')
        else:
            print(d[c.lower()].upper(), end='')
    else:
        print(c, end='')
