from itertools import combinations

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

cmb = combinations([i for i in range(n)], 2)
cnt = 0
for i, j in cmb:
    dist = sum([(x[i][k] - x[j][k])**2 for k in range(d)])
    for m in range(int(dist**0.5) + 1):
        if m**2 == dist:
            cnt += 1
print(cnt)
