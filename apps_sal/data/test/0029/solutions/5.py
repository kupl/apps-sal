from functools import reduce
e = input()
mi = 6
for i in range(1000000):
    a = str(i).zfill(6)
    s = ord(a[0]) + ord(a[1]) + ord(a[2])
    t = ord(a[3]) + ord(a[4]) + ord(a[5])
    if s == t:
        l = sum(list([0 if x[0] == x[1] else 1 for x in zip(a, e)]))
        mi = min(mi, l)
print(mi)
