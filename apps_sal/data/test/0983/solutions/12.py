(n, p, q, r) = [int(i) for i in input().split()]
aa = [int(i) for i in input().split()]
max_from_p = []
m = None
for i in range(n):
    if i == 0:
        m = aa[i] * p
    elif aa[i] * p > m:
        m = aa[i] * p
    max_from_p.append(m)
max_from_pq = []
m = None
for i in range(n):
    if i == 0:
        m = aa[i] * q + max_from_p[i]
    elif aa[i] * q + max_from_p[i] > m:
        m = aa[i] * q + max_from_p[i]
    max_from_pq.append(m)
m = None
for i in range(n):
    if i == 0:
        m = aa[i] * r + max_from_pq[i]
    elif aa[i] * r + max_from_pq[i] > m:
        m = aa[i] * r + max_from_pq[i]
print(m)
