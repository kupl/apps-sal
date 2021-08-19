a = input()
t1 = 0
t2 = 0
t3 = 0
t4 = 0
ind1 = 0
ind2 = 0
ind3 = 0
ind4 = 0
for j in range(len(a)):
    if a[j] == 'R':
        ind1 = j % 4
    if a[j] == 'B':
        ind2 = j % 4
    if a[j] == 'Y':
        ind3 = j % 4
    if a[j] == 'G':
        ind4 = j % 4
for j in range(len(a)):
    if a[j] == '!':
        if j % 4 == ind1:
            t1 += 1
        elif j % 4 == ind2:
            t2 += 1
        elif j % 4 == ind3:
            t3 += 1
        else:
            t4 += 1
print(t1, t2, t3, t4)
