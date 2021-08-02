# WHY IS RUBY SO SLOW????
input()
a = [*list(map(int, input().split()))]
r = {}
for i, x in enumerate(list(set(a))):
    r[x] = i
n = len(r)
m = 0
a = [r[x] for x in a]
for i, x in enumerate(a):
    h = [0 for _ in range(n)]
    l = [-2 for _ in range(n)]
    lx = -1
    for j, y in enumerate(a[i + 1:]):
        if y == x:
            lx = j
        if l[y] < lx:
            h[y] += 1
        l[y] = j
    for k in range(n):
        if k == x:
            h[k] = h[k] + 1
        elif l[k] < lx:
            h[k] = 2 * h[k] + 1
        else:
            h[k] = 2 * h[k]
    m = max(m, max(h + [1]))
print(m)
