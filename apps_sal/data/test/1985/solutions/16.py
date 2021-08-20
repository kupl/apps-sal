def o():
    return [int(f) for f in input().split()]


(k, n) = o()
a = o()
b = o()
s = []
for x in b:
    t = x
    t1 = set()
    for y in a:
        t -= y
        t1.add(t)
    s += [t1]
print(len(set.intersection(*s)))
