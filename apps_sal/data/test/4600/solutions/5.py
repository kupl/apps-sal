(n, m) = map(int, input().split())
ac = set()
(w, x) = (0, [0 for i in range(n)])
for i in range(m):
    (p, s) = input().split()
    l = int(p) - 1
    if not l in ac:
        if s == 'AC':
            ac.add(l)
            w += x[l]
        else:
            x[l] += 1
print(len(ac), w)
