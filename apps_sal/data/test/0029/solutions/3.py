s = input()
l = []
for d in s[:3]:
    l.append(int(d))
u = []
for d in s[3:]:
    u.append(int(d))
if sum(l) == sum(u):
    print(0)
else:
    if sum(l) > sum(u):
        (l, u) = (u, l)
    diffs = sorted(list([9 - x for x in l]) + u)[::-1]
    for i in range(1, 7):
        if sum(diffs[:i]) >= sum(u) - sum(l):
            print(i)
            break
