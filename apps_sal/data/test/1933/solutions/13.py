n, m, k = map(int, input().split())
ar = []

for i in range(n):
	ar.append(list(map(int, input().split())))

score = 0
min_moves = 0
for j in range(m):
	cr = [ar[i][j] for i in range(n)]
	c = 0
	maxi = 0
	r_s = 0
	r_m = 0
	for i in range(len(cr)):
		if cr[i] == 1:
			maxi = sum(cr[i:i+k])
			if maxi > r_s:
				r_s = maxi
				r_m = c
			c += 1

	score += r_s
	min_moves += r_m

print(score, min_moves)
