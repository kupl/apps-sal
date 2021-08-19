def R():
    return list(map(int, input().split()))


(n, m, k) = R()
l = R()
q = 0
t = 1
nb = 0
for i in range(m - 1):
    if (l[i + 1] - 1 - q) // k == (l[i] - 1 - q) // k:
        t += 1
        pass
    else:
        nb += 1
        q += t
        t = 1
print(nb + 1)
