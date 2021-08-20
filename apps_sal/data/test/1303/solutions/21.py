(p, q, l, r) = (int(x) for x in input().split())
(tx, val) = ([], [False] * (r - l + 1))
for i in range(p):
    tx.append([int(x) for x in input().split()])
for i in range(q):
    (c, d) = (int(x) for x in input().split())
    for x in tx:
        for j in range(max(l, x[0] - d), min(r, x[1] - c) + 1):
            val[j - l] = True
print(sum(val))
