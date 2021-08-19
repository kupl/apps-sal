n = int(input())
(ps, qs) = ([], [])
for _ in range(n):
    (p, q) = list(map(int, input().split()))
    ps.append(p)
    qs.append(q)
ps.sort(reverse=True)
qs.sort(reverse=True)
res = n
for i in range(n):
    res += max(ps[i], qs[i])
print(res)
