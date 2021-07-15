a, b, c = list(map(int,input().split()))
chuj = ['a', 'b', 'c', 'a', 'c', 'b', 'a', 'a', 'b', 'c', 'a', 'c', 'b', 'a']
p = min(a // 3, b // 2, c // 2)
a = a - p * 3
b = b - p * 2
c = c - p * 2
wyn = 7 * p
res = 0
for i in range(7):
	pom = 0
	aa = a
	bb = b
	cc = c
	for j in range(7):
		if chuj[i + j] == "a":
			aa -= 1
		if chuj[i + j] == "b":
			bb -= 1
		if chuj[i + j] == "c":
			cc -= 1
		if aa < 0 or bb < 0 or cc < 0:
			res = max(pom,res)
			break
		pom += 1
print(res+wyn)
