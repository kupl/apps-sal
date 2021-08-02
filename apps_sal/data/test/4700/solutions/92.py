n, m = map(int, input().split())
h = list(map(int, input().split()))
l = list({i} for i in range(n + 1))
for i in range(m):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)

for i in range(len(l)):
    l[i] = list(l[i])
good = set()
for i in range(1, len(l)):
    l[i].remove(i)
    for j in range(len(l[i])):
        if h[l[i][j] - 1] >= h[i - 1]:
            break
    else:
        good.add(i)
print(len(good))
