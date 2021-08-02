n = int(input())
a = []
x = []
y = []
for i in range(n):
    z = int(input())
    a.append(z)
    for j in range(z):
        s, r = map(int, input().split())
        x.append(s)
        y.append(r)
ans = 0
for i in range(2**n):
    t = [0] * n
    j = 0
    k = 0
    z = i
    while z > 0:
        if z % 2 != 0:
            t[j] = 1
            k += 1
        j += 1
        z = z // 2
    flg = True
    j = 0
    z = 0
    p = 0
    while j < n:
        if t[j] == 1:
            for q in range(a[z]):
                if t[x[p + q] - 1] != y[p + q]:
                    flg = False
        p += a[z]
        j += 1
        z += 1
    if flg:
        ans = max(ans, k)
print(ans)
