#! /usr/bin/python3

n = int(input())
a = list(map(int, input().split()))
#a = tuple(map(int, input().split()))
u = {}
v = {}
w = []

for i, x in enumerate(a):
    if x in v:
        v[x].append(i)
    else:
        v[x] = [i]

for x, li in list(v.items()):
    if len(li) == 1:
        w.append((x, 0))
    else:
        s = set([li[i] - li[i - 1] for i in range(1, len(li))])
        if len(s) == 1:
            w.append((x, s.pop()))

print(len(w))

print('\n'.join('%d %d' % x for x in sorted(w)))
