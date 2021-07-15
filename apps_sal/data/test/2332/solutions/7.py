n, k, m = list(map(int,input().split()))
d = list(map(str,input().split()))
dic = dict()
co = list(map(int,input().split()))
for i in range(k):
	l = list(map(int,input().split()))
	p = []
	for i in range(1, l[0] + 1):
		p += [[co[l[i] - 1], d[l[i] - 1]]]
	u = min(p)
	for i in range(1, l[0] + 1):
		dic[d[l[i] - 1]] = u
poi = list(map(str,input().split()))
cost = 0
for i in range(m):
	cost += dic[poi[i]][0]
print(cost)

