((x, y, a, b, c), p, q, r) = [[*list(map(int, i.split()))] for i in open(0)]
p = sorted(p)[-x:]
q = sorted(q)[-y:]
pq = sorted(p + q)
r.sort(reverse=True)
ans = sum(pq)
for i in range(min(c, x + y)):
    if r[i] > pq[i]:
        ans += r[i] - pq[i]
    else:
        break
print(ans)
