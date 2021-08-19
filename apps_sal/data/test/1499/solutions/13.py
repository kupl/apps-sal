a = input().split()
b = int(a[0])
c = int(a[1])
l1 = []
l2 = []
l3 = []
l4 = []
for i in range(1, c + 1):
    if i <= 2 * b:
        if i % 2 == 1:
            l1.append(i)
        else:
            l4.append(i)
    elif i % 2 == 1:
        l2.append(i)
    else:
        l3.append(i)
l = []
i = 0
while i <= int(c) + 1:
    try:
        l.append(l2[i])
    except:
        pass
    try:
        l.append(l1[i])
    except:
        pass
    try:
        l.append(l3[i])
    except:
        pass
    try:
        l.append(l4[i])
    except:
        pass
    i += 1
s = ''
for i in l:
    s = s + str(i) + ' '
print(s)
