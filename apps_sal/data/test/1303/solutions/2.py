p, q, x, y = list(map(int, input().split()))
a = [0 for i in range(p)]
b = [0 for i in range(p)]
c = [0 for i in range(q)]
d = [0 for i in range(q)]
for i in range(p):
    a[i], b[i] = list(map(int, input().split()))
for i in range(q):
    c[i], d[i] = list(map(int, input().split()))


ans = 0


def comp(k, l, m, n):
    if m <= l and k <= n:
        return 0
    elif m >= l:
        return 1
    else:
        return -1


for t in range(x, y + 1):
    i = 0
    j = 0
    while i < p and j < q:
        z = comp(a[i], b[i], c[j] + t, d[j] + t)

        if z == 0:
            ans += 1
            break
        elif z == 1:
            i += 1
        else:
            j += 1

print(ans)
