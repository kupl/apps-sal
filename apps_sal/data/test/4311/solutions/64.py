s = int(input())
list_a = [s]
if s % 2 == 0:
    s = s / 2
else:
    s = 3 * s + 1
current = 2
while s not in list_a:
    list_a.append(s)
    if s % 2 == 0:
        s = s / 2
    else:
        s = 3 * s + 1
    current += 1
print(current)
