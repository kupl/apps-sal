def change(score1,score2):
	if score1==None:
		return min(score2)+1
	max_1=max(score1[0],score2[0])
	max_2=max(score1[1],score2[1])
	min_1=min(score1[0],score2[0])
	min_2=min(score1[1],score2[1])
	return max(0,min(max_1,max_2)-max(min_1,min_2)+(not(score1[0]==score1[1])))
scores=None
ans=0
for i in range(int(input())):
	temp=[int(i) for i in input().split()]
	if temp==scores:
		continue
	ans+=change(scores,temp)
	scores=temp[:]
print(ans)

