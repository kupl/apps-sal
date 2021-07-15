import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for x in range(n):
	l.append(input().strip())
points = list(map(int, input().split()))
cnts = [0 for i in range(m)]
t = [0, 0, 0, 0, 0]
for i in range(m):
	t = [0, 0, 0, 0, 0]
	for x in l:
		choice = x[i]
		t[ord(choice) - 65] += 1
	cnts[i] = max(t)
#print(cnts)
print(sum(i[0] * i[1] for i in zip(points, cnts)))
