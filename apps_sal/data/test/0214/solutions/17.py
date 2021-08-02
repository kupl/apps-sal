r1 = input()
r2 = input()
n = len(r1)
l = [0]
for i in range(n):
    if r1[i] == '0':
        if r2[i] == '0':
            l.append(2)
        else:
            l.append(1)
    else:
        if r2[i] == 'X':
            l.append(0)
        else:
            l.append(-1)
l.append(0)
s = len(l)
count = 0
u = 1
e = 1
while(u < s - 1):
    if l[u] == 2 and e == 1:
        if l[u + 1] == 2:
            e = 2
            u = u + 1
            continue
        elif (l[u + 1] == 1 or l[u + 1] == -1):
            count = count + 1
            u = u + 2
            continue
        else:
            u = u + 2
            continue
    if l[u] == 2 and e == 2:
        if l[u + 1] == 2:
            count = count + 2
            u = u + 2
            e = 1
            continue
        else:
            count = count + 1
            u = u + 1
            e = 1
            continue
    if l[u] == 1 or l[u] == -1:
        if l[u + 1] == 2:
            count = count + 1
            u = u + 2
            continue
        else:
            u = u + 1
            continue
    if l[u] == 0:
        u = u + 1
print(count)
