
l1 = []
l2 = []
for i in input():
    l1.append(i)
for i in input():
    l2.append(i)
count = 0
c = 0
while c < len(l1) - 1:
    newli = [l1[c], l1[c + 1], l2[c], l2[c + 1]]
    try:
        if l1[c] == l1[c + 1] == l1[c + 2] == l2[c] == l2[c + 1] == l2[c + 2] == '0':
            count += 2
            c += 3
            continue
    except:
        pass
    if newli.count('0') >= 3:
        count += 1
        c += 2
    else:
        c += 1
print(count)
