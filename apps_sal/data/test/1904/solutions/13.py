n = int(input())
s = input()
data = input().split()
a = [0 for i in range(n + 1)]
d = [[0 for i in range (5)] for j in range(n + 1)]
c = ['w', 'h', 'a', 'r', 'd']
for i in range(1, n + 1): 
	a[i] = int(data[i - 1])

s = '0' + s

for i in range (1, n + 1):
	if s[i] == c[1]:
		d[i][1] = d[i - 1][1] + a[i]
	else: d[i][1] = d[i - 1][1]

for j in range (2, 5):
	for i in range(1, n + 1):
		if s[i] == c[j]:
			d[i][j] = min(d[i - 1][j - 1], d[i - 1][j] + a[i])
		else: d[i][j] = d[i - 1][j]

print(d[n][4])
