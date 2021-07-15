d = list(map(int, input().split()))
n = d[0]
h = d[1]
a = d[2]
b = d[3]
k = d[4]

ans = []

for i in range(k):
	t = 0
	d = list(map(int, input().split()))
	ta = d[0]
	fa = d[1]
	tb = d[2]
	fb = d[3]
	
	if ta == tb:
		ans.append(abs(fa - fb))
	else:
		if fa > b:
			ans.append((fa-b)+abs(ta-tb)+abs(b-fb))
		elif fa < a:
			ans.append((a-fa)+abs(ta-tb)+abs(a-fb))
		else:
			ans.append(abs(ta-tb)+abs(fa-fb))
			
for i in range(k):
	print(ans[i])
	


