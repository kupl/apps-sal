g = [[] for _ in range(100005)]

n, m = list(map(int, input().split(' ')))
for i in range(m):
    a, b = list(map(int, input().split(' ')))
    g[a].append(b)
    g[b].append(a)

colour = [0] * 100005
v = [0] * 100005

cycle = False
two = True
twos = 0
ones = 0
ans = 0
for i in range(1, n + 1):
    cs = 0
    c1 = 0
    c2 = 0
    if (not colour[i]):
        q = [i]
        colour[i] = 1
        while q:
            cs += 1
            top = q.pop()
            if colour[top] == 1:
                c1 += 1
            else:
                c2 += 1
            for j in g[top]:
                if colour[j] == colour[top]:
                    cycle = True
                elif colour[j] == 0:
                    colour[j] = -colour[top]
                    q = [j] + q
        if cs > 2:
            two = False
            ans += ((c1 * (c1 - 1)) // 2 + (c2 * (c2 - 1)) // 2)
        if cs == 2:
            twos += 1

        if cs == 1:
            ones += 1
if cycle:
    print(0, 1)
    quit()

if m == 0:
    print(3, (n * (n - 1) * (n - 2) // 6))
    quit()
if two:
    print(2, twos * ones + 4 * (twos * (twos - 1) // 2))
    quit()
sumx = 0
for i in range(1, n + 1):
    ll = len(g[i])
    sumx += ll * (ll - 1) // 2
print(1, ans)
