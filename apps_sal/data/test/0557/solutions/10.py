import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline

n, m = map(int, read().split())
cango = 0
for _ in range(n):
	point, limit = map(int, read().split())
	if cango >= point and limit > cango:
		cango = limit
if cango >= m:
	print("YES")
else:
	print("NO")
