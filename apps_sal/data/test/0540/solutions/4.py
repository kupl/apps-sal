#file = open('test.txt', 'r')
def recurse():
	nonlocal ans
	qu = []
	qu.append((r1, c1))
	count = 1
	i = 0
	while i < count:
		r, c = qu[i]
		if r == r2 and c == c2:
			ans = True
			return
		
		mas[r][c] = 1
			
		if mas[r + 1][c] == 0:
			#recurse(r + 1, c)
			qu.append((r + 1, c))
			mas[r + 1][c] = 1
			count += 1
		if mas[r - 1][c] == 0:
			#recurse(r - 1, c)
			qu.append((r - 1, c))
			mas[r - 1][c] = 1
			count += 1
		if mas[r][c + 1] == 0:
			#recurse(r, c + 1)
			qu.append((r, c + 1))
			mas[r][c + 1] = 1
			count += 1
		if mas[r][c - 1] == 0:
			#recurse(r, c - 1)
			qu.append((r, c - 1))
			mas[r][c - 1] = 1
			count += 1
		i += 1

n, m = [int(x) for x in input().split()]
#n, m = [int(x) for x in file.readline().split()]
mas = []
mas.append([-1] * (m + 2))
for i in range(1, n + 1):
	mas.append([0] * (m + 2))
mas.append([-1] * (m + 2))

for i in range(1, n + 1):
	mas[i][0] = mas[i][m + 1] = -1

for i in range(1, n + 1):	
	s = input()
	#s = file.readline()
	for j in range(1, m + 1):
		if s[j - 1] == 'X':
			mas[i][j] = -1

r1, c1 = [int(x) for x in input().split()]
r2, c2 = [int(x) for x in input().split()]
#r1, c1 = [int(x) for x in file.readline().split()]
#r2, c2 = [int(x) for x in file.readline().split()]

her = 0
if mas[r2 - 1][c2] != -1:
	her += 1
if mas[r2 + 1][c2] != -1:
	her += 1
if mas[r2][c2 - 1] != -1:
	her += 1
if mas[r2][c2 + 1] != -1:
	her += 1
if r1 == r2 and c1 == c2:
	if her > 0:
		print("YES")
	else:
		print("NO")
elif abs(r1 - r2) + abs(c1 - c2) == 1:
	if mas[r2][c2] != 0 or her > 0:
		print("YES")
	else:
		print("NO")
else:
	ans = False
	z = mas[r2][c2]
	mas[r1][c1] = mas[r2][c2] = 0
	recurse()
	#mas[r2][c2] = z
	if not ans:
		print("NO")
	elif z != 0:
		print("YES")
	else:
		if her > 1:
			print("YES")
		else:
			print("NO")
