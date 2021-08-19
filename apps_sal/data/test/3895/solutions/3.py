n = int(input())
f = [None] + list(map(int, input().split(' ')))
invalid = False
g = [None] + [0] * n
h = [None]
x_is_f_which = [None] + [0] * n
m = 0
vis = [None] + [False] * n
for i in range(1, n + 1):
    x = f[i]
    if f[x] != x:
        invalid = True
        break
    if not vis[x]:
        vis[x] = True
        m = m + 1
        h.append(x)
        x_is_f_which[x] = m
if invalid:
    print('-1')
else:
    for i in range(1, n + 1):
        g[i] = x_is_f_which[f[i]]
    print(m)

    def print_list(l):
        print(' '.join(list(map(str, l[1:]))))
    print_list(g)
    print_list(h)
