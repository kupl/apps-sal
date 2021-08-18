n, q = list(map(int, input().split()))
nn = (n**2 + 1) // 2

a = []
kv_n = n * n
pol_n = n // 2
for i in range(q):
    y, x = list(map(int, input().split()))
    if y > pol_n:
        spes = kv_n - (n - y + 1) * n
    else:
        spes = (y - 1) * n
    if (x + y) % 2 == 0:
        a.append(str((spes + x + 1) // 2))
    else:
        a.append(str(nn + (spes + x + 1) // 2))
print('\n'.join(a))
