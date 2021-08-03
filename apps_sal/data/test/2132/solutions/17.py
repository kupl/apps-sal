p = [1e9]
d = k = v = 0
for i in range(int(input())):
    s = input()
    t = int(s[0])
    if t == 1:
        v = int(s[2:])
        while p[-1] < v:
            p.pop()
            k += 1
    if t == 2:
        k, d = k + d, 0
    if t == 3:
        u = int(s[2:])
        if v > u:
            k += 1
        else:
            p += [u]
    if t == 4:
        d = 0
    if t == 5:
        p = [1e9]
    if t == 6:
        d += 1
print(k)
