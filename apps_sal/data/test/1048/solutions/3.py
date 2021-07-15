n = int(input())
s = input()
d = {'L': (-1, 0), 'U': (0, 1), 'D': (0, -1), 'R': (1, 0)}

u, v = 0, 0

for c in s:
	u += d[c][0]
	v += d[c][1]

print(n - abs(u) - abs(v))

