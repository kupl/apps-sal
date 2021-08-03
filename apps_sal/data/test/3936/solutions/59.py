n = int(input())
a = input()
b = input()
if a[0] == b[0]:
    c = 3
    i = 1
    d = 0
else:
    c = 6
    i = 2
    d = 1

while i < n:
    if a[i] == b[i]:
        if d == 0:
            c = (c * 2) % (10**9 + 7)
        else:
            d = 0
    else:
        i += 1
        if d == 0:
            c = (c * 2) % (10**9 + 7)
            d = 1
        else:
            c = (c * 3) % (10**9 + 7)
    i += 1
print(c)
