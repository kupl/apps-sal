def re():
    return [int(x) for x in input().split(' ')]


[n, m] = re()
us = re()
us.sort()

ar = []
k = 0
i = 0
if len(us) == 0:
    i = 1
    while m > 0:
        if m - i >= 0 and i != us[0]:
            ar.append(str(i))
            m -= i
            i += 1
        else:
            i += 1
if us[0] > 1:
    i = 1
    while m > 0 and i != us[0]:
        if m - i >= 0:
            m -= i
            ar.append(str(i))
            i += 1
        else:
            break
i = 0
while i < len(us) - 1:
    for j in range(us[i] + 1, us[i + 1]):
        if m - j >= 0:
            ar.append(str(j))
            m -= j
        else:
            i = len(us)
            break
    i += 1
if m > 0 and m > us[-1]:
    i = us[-1] + 1
    while m > 0:
        if m - i >= 0:
            m -= i
            ar.append(str(i))
            i += 1
        else:
            break
print(len(ar))
print(" ".join(ar))
