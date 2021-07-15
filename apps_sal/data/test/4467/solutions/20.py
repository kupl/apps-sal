N=int(input())
AB=sorted([list(map(int, input().split())) for _ in range(N)])
CD=sorted([list(map(int, input().split())) for _ in range(N)])

paira=-1
pairb=-1
ans=0

for i in range(N):
	tempcd=CD[i]
	for h in range(len(AB)):
		tempab=AB[h]
		if tempab[0]<tempcd[0] and tempab[1]<tempcd[1]:
			if pairb<tempab[1]:
				paira=tempab[0]
				pairb=tempab[1]
				pairnum=h
	if paira!=-1 and pairb!=-1:
		ans+=1
		AB.pop(pairnum)
		paira=-1
		pairb=-1

print(ans)
			

