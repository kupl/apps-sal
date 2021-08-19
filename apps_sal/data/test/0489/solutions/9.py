n = int(input())
a = [int(x) for x in input().split()]
a.sort()
l = [a[0], a[1], a[2]]
mx = 0
val = l.count(l[0])
val2 = l.count(l[1])
val3 = l.count(l[2])
if val == 2:
    val = a.count(l[2])
    mx = max(mx, val)
elif val == 3:
    val = a.count(l[0])
    val = val * (val - 1) * (val - 2) // 6
    mx = max(mx, val)
elif val2 == 2:
    val = a.count(l[1])
    val = val * (val - 1) // 2
    mx = max(mx, val)
else:
    for i in l:
        mx = max(mx, a.count(i))
print(mx)
