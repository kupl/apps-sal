n, m, q = list(map(int,input().split()))
timeR, timeC, color = [0] * n, [0] * m, [0] * (q + 1)

for query in range(1, q + 1):
	typeQ, posQ, color[query] = list(map(int, input().split()))
	if typeQ == 1:
		timeR[posQ - 1] = query
	else:
		timeC[posQ - 1] = query

for i in range(n):
	out = str()
	for j in range(m):
		out += str(color[max(timeR[i], timeC[j])])
		out += " "
	print(out)

