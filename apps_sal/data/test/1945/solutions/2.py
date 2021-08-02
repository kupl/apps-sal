# /usr/bin/env python3

N = int(input())
names = [input().split() for i in range(N)]

c_to_old = dict()

for n in names:
    if n[0] not in c_to_old:
        c_to_old[n[1]] = n[0]
    else:
        old = c_to_old[n[0]]
        del c_to_old[n[0]]
        c_to_old[n[1]] = old

print(len(c_to_old))
thing = sorted(list(c_to_old.items()), key=lambda x: x[1])
for c, o in thing:
    print(o, c)
