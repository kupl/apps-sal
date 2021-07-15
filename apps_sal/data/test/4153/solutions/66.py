S=list(input())[::-1]
que=[]
N=len(S)
ans=0

while len(S)>0:
	que.append(S.pop(-1))
	if len(que)>1:
		if (que[-1]=="1" and que[-2]=="0") or (que[-1]=="0" and que[-2]=="1"):
			que.pop(-1)
			que.pop(-1)
			ans+=2

print(ans)
