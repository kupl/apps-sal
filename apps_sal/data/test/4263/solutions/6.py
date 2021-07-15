def judge(c):
	if c=='A' or c=='G' or c == 'C' or c == 'T':
		return True
	else:
		return False

s = input()

ans = 0

for i in range(0,len(s)):
	for j in range(i+1,len(s)+1):
		ok = True
		for k in range(i,j):
			#print(i,j,k)
			if not judge(s[k]):
				ok = False
		if ok:
			ans = max(ans,j-i)

print(ans)
