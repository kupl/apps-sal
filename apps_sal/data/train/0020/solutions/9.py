q = int(input())
for rewrew in range(q):
	n, t0 = map(int,input().split())
	t = []
	l = []
	h = []
	for i in range(n):
		tt,ll,hh = map(int,input().split())
		t.append(tt)
		l.append(ll)
		h.append(hh)
	possib = [[0,0]]*n
	dasie = True
	possib[0] = [-t[0]+t0,t[0]+t0]
	for i in range(n):
		if l[i]>possib[i][1] or h[i] < possib[i][0]:
			dasie = False
			break
		else:
			possib[i][0] = max(possib[i][0],l[i])
			possib[i][1] = min(possib[i][1], h[i])
		if i < n-1:
			possib[i+1][0] = possib[i][0] - (t[i+1]-t[i])
			possib[i+1][1] = possib[i][1] + (t[i+1]-t[i])
	if dasie:
		print("YES")
	else:
		print("NO")
