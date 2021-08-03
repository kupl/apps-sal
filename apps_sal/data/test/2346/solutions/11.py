3


def ir(): return int(input())
def ia(): return [int(i) for i in input().split()]


n = ir()

p = [None] * n
c = [None] * n
adj = [[] for i in range(n)]

good = [False] * n

for i in range(n):
    p0, c0 = ia()
    c[i] = c0
    if p0 == -1:
        p[i] = p0
        good[i] = True
    else:
        p0 -= 1
        p[i] = p0
        adj[p0].append(i)
        if c0 == 0:
            good[i] = True
            good[p0] = True

ans = []
for i, e in enumerate(good):
    if not e:
        ans.append(i)

ans.sort()

if ans == []:
    print(-1)
else:
    ans = [str(e + 1) for e in ans]
    print(" ".join(ans))
