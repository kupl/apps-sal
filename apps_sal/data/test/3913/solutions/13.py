n = int(input())
s = input()
m = int(input())
l = []
cnt_ = []
cnt = []
for i in range(n):
	if s[i]=='*':
		cnt_.append(i)
	else: cnt.append(i)
for x in range(m):
	flag = True
	st = input()
	for j in cnt_:
		if st[j] in s:
			flag = False
	else:
		for j in cnt:
			if st[j]!=s[j]: flag =False
	if flag:
		l.append(st)
g = [[] for i in range(len(l))]
for i in range(len(l)):
	for j in cnt_:
		g[i].append(l[i][j])
for i in range(len(g)):
	g[i] = list(set(g[i]))
ans = 0
for ch in g[0]:
	for li in g:
		if ch not in li: break
	else: ans = ans+1
print(ans)
