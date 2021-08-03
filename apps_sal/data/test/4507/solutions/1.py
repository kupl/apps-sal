IN = input
def rint(): return int(IN())
def rmint(): return list(map(int, IN().split()))
def rlist(): return list(rmint())


n, m, k = rmint()
a = rlist()
t = []
for i in range(m):
    x, y = rmint()
    t.append((x, y))
t.sort()
a.sort()
pr = [0]
for i in a:
    pr.append(pr[-1] + i)
f = 4096 * [0]


def s(l, r):
    if l > r:
        return 0
    else:
        return pr[r + 1] - pr[l]


ans = s(0, k - 1)


def upd(x, y):
    nonlocal ans
    f[x] = min(f[x], y)
    ans = min(ans, y + s(x, k - 1))


for i in range(1, k + 1):
    f[i] = f[i - 1] + a[i - 1]
    for p in t:
        x, y = p
        if i - x < 0:
            break
        upd(i, f[i - x] + s(i - x + y, i - 1))

print(ans)
