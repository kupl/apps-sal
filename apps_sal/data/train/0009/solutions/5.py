def solv():
	s=list(map(int,input()))
	v=[]
	sm=0
	for n in s:
		if n:
			sm+=1
		else:
			v.append(sm)
			sm=0
	if sm:v.append(sm)
	v.sort(reverse=True)

	res=0

	for n in range(0,len(v),2):res+=v[n]
	print(res)

for _ in range(int(input())):solv()
