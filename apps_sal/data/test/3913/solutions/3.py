n = int(input())
s = input()
lr = []
r = []
w = set()
for i in range(len(s)):
    if s[i] == '*':
        lr.append(i)
    else:
        r.append(i)
        w.add(s[i])
m = int(input())
k = None
for i in range(m):
    e = input()
    f = False
    for j in lr:
        if e[j] in w:
            f = True
            break
    for j in r:
        if e[j] != s[j]:
            f = True
            break
    if f:
        continue
    if k is None:
        k = set((e[i] for i in lr))
    else:
        u = set((e[i] for i in lr))
        k = k.intersection(u)
print(len(k))
