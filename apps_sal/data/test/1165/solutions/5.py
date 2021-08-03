from sys import stdin

n, m = map(int, stdin.readline().split())
a = stdin.readline().split()

pre = []
t, index = a[0], 0
for i in range(n):
    index = index if a[i] == t else i
    t = a[i]
    pre.append(index)

prt = []
for i in range(m):
    l, r, x = stdin.readline().split()
    l, r = int(l), int(r)
    L = pre[r - 1]
    if a[r - 1] == x:
        sl = pre[r - 1] + 1
        if sl <= l:
            prt.append(str(-1))
            continue
        r = sl - 1
    prt.append(str(r))

print("\n".join(prt))
