a = []
i = 1
while len(a) <= 10000:
    l = str(i)
    for p in l:
        a.append(p)
    i += 1

g = int(input())
print(a[g - 1])
