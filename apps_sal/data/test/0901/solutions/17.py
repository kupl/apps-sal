n, m = [int(i) for i in input().split()]

def check(line):
	for i in line:
		if -i in line:
			return True
	return False
	
for _ in range(m):
	line = set([int(i) for i in input().split()][1:])
	if not check(line):
		print('YES')
		return

print('NO')

