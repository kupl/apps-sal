s = [x for x in input()]
t = [x for x in input()]
u = list()
for i in range(len(s) - len(t) + 1):
    count = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            continue
        if s[i+j] != t[j]:
            count += 1
    u.append(count)
u.sort()
print(u[0])
