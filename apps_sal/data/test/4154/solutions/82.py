(n, m) = list(map(int, input().split()))
(l, r) = ([], [])
for i in range(m):
    (a, b) = list(map(int, input().split()))
    l.append(a)
    r.append(b)
ans = max(0, min(r) - max(l) + 1)
print(ans)
