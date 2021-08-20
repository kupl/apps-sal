n = int(input())
a = list(map(int, input().split()))
m = int(input())
v = [0] * n
f = list(range(1, n + 1))
l = []
for i in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        (p, x) = (q[1], q[2])
        u = []
        j = p - 1
        while j < n:
            z = x + v[j] - a[j]
            if z <= 0:
                v[j] += x
                break
            else:
                x = z
                v[j] = a[j]
                u.append(j)
                j = f[j]
        for z in u:
            f[z] = j
    else:
        l.append(v[q[1] - 1])
print(*l, sep='\n')
