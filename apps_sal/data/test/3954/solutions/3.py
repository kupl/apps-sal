from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
t = list(map(int, input().split()))
p = sorted(t)

if p[-1] <= 0:
    print(p[-1])
    return
if p[0] >= 0:
    print(sum(p))
    return
i = max(0, n - k - 1)
while p[i] < 0: i += 1
q = sum(p[i: ])
if n < k + 2 or p[n - k - 1] <= 0:
    print(q)
    return

for l in range(n - k - 2):
    r = l + k + 2
    u = sorted(t[: l] + t[r: ])
    v = sorted(t[l: r])
    for i in range(r, n):
        q = max(q, sum(sorted(v + u[- min(k, len(u)): ])[- len(v): ]))
        u.remove(t[i])
        v.insert(bisect_left(v, t[i]), t[i])
    q = max(q, sum(sorted(v + u[- min(k, len(u)): ])[- len(v): ]))
print(q)
