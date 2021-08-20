def mp():
    return map(int, input().split())


(n, m) = mp()
a = list(mp())
b = list(mp())
n1 = n2 = c1 = c2 = 0
for i in a:
    if i % 2 == 0:
        c1 += 1
    else:
        n1 += 1
for i in b:
    if i % 2 == 0:
        c2 += 1
    else:
        n2 += 1
print(min(c1, n2) + min(c2, n1))
