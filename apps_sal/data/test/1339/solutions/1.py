import sys
f = sys.stdin
n = int(f.readline().strip())
(l, r) = ([], [])
for line in f:
    l.append(int(line.strip().split()[0]))
    r.append(int(line.strip().split()[1]))
ls = list(set(l))
rs = list(set(r))
ls.sort()
rs.sort(reverse=True)
ind = -1
for i in range(n):
    if l[i] <= ls[0] and r[i] >= rs[0]:
        ind = i + 1
print(ind)
