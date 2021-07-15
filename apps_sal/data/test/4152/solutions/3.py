from math import log, ceil
n = int(input())
numbers = list(map(int, input().split(" ")))

occurences = {}
for m in numbers:
    if m in list(occurences.keys()):
        occurences[m] += 1
    else:
        occurences[m] = 1

count = 0
for m in list(occurences.keys()):
    l = ceil(log(m, 2))
    found = False
    for i in range(l, 31):
        if 2 ** i - m == m:
            if occurences[m] > 1:
                found = True
                break
        elif 2 ** i - m in list(occurences.keys()):
            found = True
            break
    if not found:
        count += occurences[m]

print(count)

