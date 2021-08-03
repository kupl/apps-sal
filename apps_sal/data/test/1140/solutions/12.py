n = int(input())
m = (list(int(x) for x in input().split()))
a = max(m)
z = min(m)
ac = m.count(a)
az = m.count(z)
daz = a - z
if daz:
    dc = ac * az
else:
    dc = 0
    for i in range(ac):
        dc += i
print(daz, dc)
