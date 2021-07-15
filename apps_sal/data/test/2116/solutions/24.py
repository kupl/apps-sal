l1 = list(map(int, input().split()))
n = l1[0]
m = l1[1]
k = l1[2]
a = list(map(int, input().split()))
tot = 0
for i in range(n):
	orders = list(map(int, input().split()))
	for i in range(m):
		b = []
		val = orders[i]
		pos = a.index(val)
		tot = tot + pos + 1
		a.pop(pos)
		b.append(val)
		b = b + a
		a = b
print(tot)
