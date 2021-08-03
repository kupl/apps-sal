a = input()
a = a.split()
b = a[1]
a = a[0]
if a < b:
    d = a
    for c in range(int(b) - 1):
        d = d + a
else:
    d = b
    for c in range(int(a) - 1):
        d = d + b
print(int(d))
