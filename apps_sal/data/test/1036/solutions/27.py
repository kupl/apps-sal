n,k=map(int,input().split())
s=input()

def win(x,y):
	if x==y:
		return x
	else:
		hands=[x,y]
		if "R" not in hands:
			return "S"
		elif "S" not in hands:
			return "P"
		else:
			return "R"

for _ in range(k):
	t=s+s
	s=[]
	for i in range(n):
		s.append(win(t[i*2],t[i*2+1]))
print(s[0])
