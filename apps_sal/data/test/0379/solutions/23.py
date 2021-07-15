n, m = list(map(int, input().split()))

pzl = []
for i in range(n):
	pzl.append(list(input()))

left = m + 1
right = -1
up = n + 1
down = -1

for i in range(n):
	for j in range(m):
		if pzl[i][j] == 'X':
			if left > j:
				left = j
			if right < j:
				right = j
			if up > i:
				up = i
			if down < i:
				down = i

answ = 'YES'
for i in range(up, down + 1):
	for j in range(left, right + 1):
		if pzl[i][j] != 'X':
			answ = 'NO'
print(answ)

