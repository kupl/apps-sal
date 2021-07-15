n, k = [int(i) for i in input().split()]
rows = ['P' + input() + 'P' for i in range(n)]

def try_good(rows):
	for j in range(len(rows)):
		for i in range(1, len(rows[j]) - 1):
			if rows[j][i] == '.':
				if rows[j][i - 1] != 'S' and rows[j][i + 1] != 'S':
					rows[j] = rows[j][:i] + 'x' + rows[j][i + 1:]
					return True
	return False

def try_medium(rows):
	for j in range(len(rows)):
		for i in range(1, len(rows[j]) - 1):
			if rows[j][i] == '.':
				if rows[j][i - 1] != 'S' or rows[j][i + 1] != 'S':
					rows[j] = rows[j][:i] + 'x' + rows[j][i + 1:]
					return True
	return False

def try_bad(rows):
	for j in range(len(rows)):
		for i in range(1, len(rows[j]) - 1):
			if rows[j][i] == '.':
				rows[j] = rows[j][:i] + 'x' + rows[j][i + 1:]
				return True
	return False

for i in range(k):
	if try_good(rows) == True:
		continue
	if try_medium(rows) == True:
		continue
	try_bad(rows)

ans = 0
for r in rows:
	for i in range(len(r)):
		if r[i] == 'S':
			if i > 1 and r[i - 1] != '.' and r[i - 1] != '-':
				ans += 1
			if i < len(r) - 2 and r[i + 1] != '.' and r[i + 1] != '-':
				ans += 1

print(ans)
for r in rows:
	print(r[1:-1])	

