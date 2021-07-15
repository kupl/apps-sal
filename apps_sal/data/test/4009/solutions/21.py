n, x, y = list(map(int,input().split()))
l = input()
wyn = 0
for i in range(n):
	j = n - 1 - i
	if i == x:
		break
	if i < y:
		if l[j] == '1':
			wyn += 1
	if i == y:
		if l[j] == '0':
			wyn += 1
	if i > y:
		if l[j] == '1':
			wyn += 1
print(wyn)
