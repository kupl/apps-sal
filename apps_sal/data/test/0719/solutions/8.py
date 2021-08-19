k = int(input())
lst = []
if k <= 3000:
    a = 10
    i = 0
    while i != k:
        a += 9
        b = str(a)
        b = [int(x) for x in list(b)]
        if sum(b) == 10:
            lst.append(a)
            i += 1
elif k <= 6000:
    a = 1000027
    i = 3000
    while i != k:
        a += 9
        b = str(a)
        b = [int(x) for x in list(b)]
        if sum(b) == 10:
            lst.append(a)
            i += 1
elif k <= 8000:
    a = 2230003
    i = 6000
    while i != k:
        a += 9
        b = str(a)
        b = [int(x) for x in list(b)]
        if sum(b) == 10:
            lst.append(a)
            i += 1
else:
    a = 9010000
    i = 8000
    while i != k:
        a += 9
        b = str(a)
        b = [int(x) for x in list(b)]
        if sum(b) == 10:
            lst.append(a)
            i += 1
print(max(lst))
