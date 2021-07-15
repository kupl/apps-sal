S=input()

l=[]
for i in range(len(S)):
	l.append((abs(753-int(S[i:i+3]))))

print(min(l))
