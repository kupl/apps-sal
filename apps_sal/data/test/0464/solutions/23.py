m, n = list(map(int, input().split()))
t = [input() for i in range(m)]
c = 0
import sys
for i in range(m):
	if c == 1:
		break
	for j in range(n):
		if c == 1:
			break
		if t[i][j] == "*":
			p = [0] * 4
			p[0] = (i < m - 1 and t[i+1][j] == "*")
			p[1] = (j > 0 and t[i][j-1] == "*")
			p[2] = (i > 0 and t[i-1][j] == "*")
			p[3] = (j < n - 1 and t[i][j+1] == "*")
			if sum(p) == 4:
				c = 1
				r = i
				c = j
if c == 0:
	print("NO")
	return
else:
	i = r
	j = c
	w = 1
	while True:
		if i < m - 1 and t[i+1][j] == "*":
			i += 1
			w += 1
		else:
			break
	i = r
	j = c
	while True:
		if j > 0 and t[i][j-1] == "*":
			j -= 1
			w += 1
		else:
			break
	i = r
	j = c
	while True:
		if i > 0 and t[i-1][j] == "*":
			i -= 1
			w += 1
		else:
			break
	i = r
	j = c
	while True:
		if j < n - 1 and t[i][j+1] == "*":
			j += 1
			w += 1
		else:
			break
	h = 0
	for i in range(m):
		for j in range(n):
			if t[i][j] == "*":
				h += 1
if h != w:
	print("NO")
	return
print("YES")

