n = int(input())
l = []
r = []
for i in range(n):
    x, a = list(map(int, input().split()))
    if x < 0:
        l.append((x, a))
    else:
        r.append((x, a))
l.sort(reverse=True)
r.sort()
tot = 0
for i in range(min(len(l), len(r))):
    tot += l[0][1]
    tot += r[0][1]
    l.pop(0)
    r.pop(0)
if r != []:
    tot += r[0][1]
elif l != []:
    tot += l[0][1]
print(tot)

