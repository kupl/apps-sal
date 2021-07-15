s=input()

def solve(s):
	if s[0]==s[-1]:
		A=1 
	else:
		A=0
	if len(s)%2==0:
		B=1
	else:
		B=0
	if A+B==1:
		return("Second")
	else:
		return("First")

print(solve(s))
