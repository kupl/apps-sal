N=int(input())
S=input()
ans=[]

for i in range(len(S)):
	temp=ord(S[i])
	if temp+N>90:
		ans.append(chr(temp+N-26))
	
	else:
		ans.append(chr(temp+N))

print(("".join(ans)))

