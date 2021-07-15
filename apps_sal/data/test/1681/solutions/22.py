n = input()
m = input()
s = set(m)
area = 0
for i in s:
    a1 = n.count(i)
    a2 = m.count(i)
    if a1 == 0:
        area = -1
        break
    elif a1 >= a2:
        area += a2
    else:
        area += a1
print(area)
