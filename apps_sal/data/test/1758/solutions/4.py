n = int(input())
s = input()
t = input()
if(sorted(s)!=sorted(t)):
	print(-1)
	return
s1 = 0
s2 = 0
ans1 = 0
ans2 = 0
for i in range(len(s)):
	if(s[i]!=t[i]):
		if(s[i]=='0'):
			#a01
			if(s2>0):
				s2 -= 1
			else:
				s1 += 1
				ans1 = max(ans1, s1)
		else:
			#a10
			if(s1>0):
				s1 -= 1
			else:
				s2 += 1
				ans2 = max(ans2, s2)
print(ans1 + ans2)
