a = input()
b = input()
c = len(a)
d = len(b)
x = ""
if c <= d:
    for i in range(c):
        x = x + a[i]
        x = x + b[i]
    print(x)
if c > d:
    for i in range(d):
        x = x + a[i]
        x = x + b[i]
    x = x + a[len(a) - 1]
    print(x)
