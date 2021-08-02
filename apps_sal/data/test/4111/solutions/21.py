n = int(input())
kon = [int(x) for x in input().split()]
h = n = 0
i = 1
for item in kon:
    if i % 2 == 0:
        h += item
    else:
        n += item
    i += 1
n1 = h1 = 0
counter = 0
k = 1
for item in kon:
    if k % 2 == 0:
        i = h - h1 - item + n1
        j = n - n1 + h1
        h1 += item
    else:
        i = h - h1 + n1
        j = n - n1 + h1 - item
        n1 += item
    if i == j:
        counter += 1
    k += 1
print(counter)
