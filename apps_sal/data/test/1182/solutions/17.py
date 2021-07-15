r, c, n, k = list(map(int, input().split()))
data = [[False for i in range(c)] for j in range(r)]
for i in range(n):
	x, y = list(map(int, input().split()))
	x -= 1
	y -= 1
	data[x][y] = True
ans = 0
for a in range(r+1):
	for b in range(c+1):
		for e in range(r):
			for d in range(c):
				cnt = 0
				flag = False
				for i in range(a):
					for j in range(b):
						if 0 <= e+i < r and 0 <= d+j < c:
							if data[e+i][d+j]:
								cnt += 1
						else:
							flag = True
							break
					if flag:
						break
				if flag:
					continue
				if cnt >= k:
					ans += 1
print(ans)



