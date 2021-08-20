(m, t) = (0, [q in 'IEAOUY' for q in input()])
d = s = sum(t)
for k in range(len(t), 0, -1):
    m += d / k
    s -= t[k - 1] + t[-k]
    d += s
print(m)
