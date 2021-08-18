def dist_sq(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


n, x1, y1, x2, y2 = map(int, input().split())
R1, R2 = [], []
for i in range(n):
    x, y = map(int, input().split())
    R1.append(dist_sq(x, y, x1, y1))
    R2.append(dist_sq(x, y, x2, y2))

cand_r1 = set(R1)
cand_r1.add(0)
ans = 10**20
for r1 in cand_r1:
    r2 = 0
    for i in range(n):
        if R1[i] > r1:
            r2 = max(r2, R2[i])
    ans = min(ans, r1 + r2)
print(ans)
