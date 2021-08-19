n = int(input())
vr = [set() for x in range(0, n)]
vc = [set() for x in range(0, n)]
r = set(range(0, n))
c = set(range(0, n))
for i in range(0, n):
    s = input()
    for j in range(0, n):
        if s[j] == '.':
            vr[i].add(j)
            vc[j].add(i)
            r.discard(i)
            c.discard(j)
if len(r) == 0:
    for i in range(0, n):
        print(i + 1, vr[i].pop() + 1)
elif len(c) == 0:
    for j in range(0, n):
        print(vc[j].pop() + 1, j + 1)
else:
    print(-1)
