
n, m = list(map(int, input().split()))
k = []
f = []
for i in range(m):
    u, p = list(map(int, input().split()))
    k.append(u)
    f.append(p)


def ok(x):
    for i in range(m):
        if (k[i] - 1) // x + 1 != f[i]:
            return False
    return True


a = []
for i in range(1, 101):
    if(ok(i)):
        a.append((n - 1) // i + 1)
if len(list(set(a))) == 1:
    print(a[0])
else:
    print(-1)
