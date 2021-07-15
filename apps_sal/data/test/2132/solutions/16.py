n = int(input())
v = int(input()[2:])
p = [1e9]
d = k = 0
for i in range(n - 1):
    s = input()
    t = int(s[0])
    if t == 1:
        v = int(s[2:])
        while p[-1] < v:
            p.pop()
            k += 1
    if t == 2:
        k += d
        d = 0
    if t == 3:
        u = int(s[2:])
        if v > u: k += 1
        else: p.append(u)
    if t == 4: d = 0
    if t == 5: p = [1e9]
    if t == 6: d += 1
print(k)
