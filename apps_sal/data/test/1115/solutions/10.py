n = int(input())
s = 0
for i in map(int, input().split()):
	s += i
m = int(input())
sol = -1
for i in range(m):
	d = list(map(int, input().split()))
	if sol == -1:
		if s >= d[0] and s <= d[1]:
			sol = s
		elif s <= d[0]:
			sol = d[0]

print(sol)

