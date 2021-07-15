n=int(input())
s=input().strip()
lw=0
lw1=0
cw=0
bf=0
wf=0
for i in s:
	if i=='(':
		if lw1>lw:
			lw=lw1
		lw1=0
		bf=1
		wf=0
	elif i==')':
		lw1=0
		if wf and bf:
			cw+=1
		bf=0
		wf=0
	elif i=='_':
		if lw1>lw:
			lw=lw1
		lw1=0
		if wf and bf:
			cw+=1
		wf=0
	else:
		if not bf:
			lw1+=1
		wf=1
if lw1>lw:
	lw=lw1
print(lw,cw)

