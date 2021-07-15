g,d,f = list(map(int, input().split()))
vratars = list(map(int, input().split()))
defenders = list(map(int, input().split()))
atackers = list(map(int, input().split()))

vratars.sort()
defenders.sort()
atackers.sort()

count = 0
while 1:
	vNeed = 1
	dNeed = 2
	aNeed = 3
	try:
		if defenders[0]<atackers[0]:
			if defenders[0] < vratars[0]:
				mn = defenders.pop(0)
				d-=1
				dNeed = 1
			else:
				mn = vratars.pop(0)
				g-=1
				vNeed = 0
		else:
			if atackers[0] < vratars[0]:
				mn = atackers.pop(0)
				f-=1
				aNeed = 2
			else:
				mn = vratars.pop(0)
				g-=1
				vNeed = 0
	except IndexError:
		# print('INDERR')
		break
	# print('need', vNeed, dNeed, aNeed)
	# print('ost', g, d, f)
	if (vNeed>g) or (dNeed>d) or (aNeed>f): break
	# print('mn ', mn)
	mx = mn*2		
	if vNeed:
		vOk = 0
		for i in vratars:
			if i>mx: break
			vOk+=1
	dOk = 0
	for i in defenders:
		if i>mx: break
		dOk+=1
	aOk = 0
	for i in atackers:
		if i>mx: break
		aOk+=1


	vC = 1
	if vNeed:
		vC = vOk

	if dNeed==1:
		dC = dOk
	else:
		dC = ((dOk-1)*dOk)/2

	if aNeed==2:
		aC = ((aOk-1)*aOk)/2
	else:
		aC = ((aOk-2)*(aOk-1)*aOk)/6

	count += vC*dC*aC
	# print('c', vC, dC, aC)
print(int(count))







