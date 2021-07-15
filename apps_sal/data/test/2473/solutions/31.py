n, k = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
INF = 10 ** 19

xy.sort()

ans = INF
for i in range(n):
	for j in range(i + k - 1, n):
		width = xy[j][0] - xy[i][0]

		y = [xy[idx][1] for idx in range(i, j + 1)]
		y.sort()

		for e1, e2 in zip(y, y[k-1:]):
			height = e2 - e1
			area = width * height
			ans = min(ans, area)

print(ans)

