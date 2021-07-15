S=list(input())
S_=list(set(S))

if len(S_)==2:
	cnt=0
	for s_ in S_:
		for i in range(4):
			if S[i]==s_:
				cnt+=1
		if cnt==2:
			cnt=0
			continue
		else:
			print("No")
			return

	print("Yes")

else:
	print("No")
