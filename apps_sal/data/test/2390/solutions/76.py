from itertools import accumulate
n, c = map(int, input().split())
sushi = [list(map(int, input().split())) for i in range(n)]

r = [sushi[0][1] - sushi[0][0]]
for i in range(1, n):
    r.append(r[-1] + sushi[i][1] - (sushi[i][0] - sushi[i - 1][0]))
l = [sushi[n - 1][1] - (c - sushi[n - 1][0])]
for i in range(n - 2, -1, -1):
    l.append(l[-1] + sushi[i][1] - ((c - sushi[i][0]) - (c - sushi[i + 1][0])))
r2 = [sushi[0][1] - 2 * sushi[0][0]]
for i in range(1, n):
    r2.append(r2[-1] + sushi[i][1] - 2 * (sushi[i][0] - sushi[i - 1][0]))
l2 = [sushi[n - 1][1] - 2 * (c - sushi[n - 1][0])]
for i in range(n - 2, -1, -1):
    l2.append(l2[-1] + sushi[i][1] - 2 * ((c - sushi[i][0]) - (c - sushi[i + 1][0])))
r = list(accumulate(r, max))
l = list(accumulate(l, max))

cand = [l[-1], r[-1]]
for i in range(n):
    if 0 <= n - i - 2 <= n - 1:
        cand.append(l2[i] + r[n - i - 2])
        cand.append(r2[i] + l[n - i - 2])

print(max(max(cand), 0))
