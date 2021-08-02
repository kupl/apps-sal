n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


da = [0] * (n + 1)
pa = [-1] * (n + 1)
sa = 0
for i in range(n):
    sa += a[i]
    if da[a[i]] == 0:
        da[a[i]] += 1
        pa[a[i]] = i
    else:
        povt_a = a[i]
        place2_a = i
        place1_a = pa[a[i]]
da[0] = -1
abs_a = da.index(0)

db = [0] * (n + 1)
pb = [-1] * (n + 1)
sb = 0
for i in range(n):
    sb += b[i]
    if db[b[i]] == 0:
        db[b[i]] += 1
        pb[b[i]] = i
    else:
        povt_b = b[i]
        place2_b = i
        place1_b = pb[b[i]]
db[0] = -1
abs_b = db.index(0)

#print(povt_a, place1_a, place2_a, abs_a)
#print(povt_b, place1_b, place2_b, abs_b)

a1 = a.copy()
b1 = b.copy()

a1[place1_a] = abs_a
b1[place1_b] = abs_b
if a1 == b1:
    print(" ".join(map(str, a1)))
    return

b1[place1_b] = b[place1_b]
b1[place2_b] = abs_b
if a1 == b1:
    print(" ".join(map(str, a1)))
    return

a1[place1_a] = a[place1_a]
a1[place2_a] = abs_a
if a1 == b1:
    print(" ".join(map(str, a1)))
    return

b1[place2_b] = b[place2_b]
b1[place1_b] = abs_b
print(" ".join(map(str, a1)))
