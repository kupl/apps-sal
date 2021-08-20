n = int(input())
a = [int(x) for x in input().split()]
b = {}
for x in a:
    if x in b:
        b[x] += 1
    else:
        b[x] = 1
summa = 0
while len(b) > 0:
    count = 0
    c = b.copy()
    for x in b:
        c[x] -= 1
        if c[x] == 0:
            c.pop(x)
        count += 1
    b = c.copy()
    summa += count - 1
print(summa)
