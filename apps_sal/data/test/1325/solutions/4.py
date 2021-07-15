import math

(n, p) = map(int, input().split(' '))
S = input()
p = min(p-1,n-p)

s1 = S[0:int(n/2)]
s2 = S[-int(n/2):]
s2 = s2[::-1]
if s1==s2:
	print(0)
	return
l = int(n/2)
r = 0
ans = 0
for i in range(0, int(n/2)):
	if s1[i]!=s2[i]:
		if i<l:
			l = i
		if i>r:
			r = i
		ans += int( min(abs(ord(s1[i])-ord(s2[i])), abs(abs(ord(s1[i])-ord(s2[i]))-26) ))
ans += int( abs(r-l)+min(abs(r-p),abs(l-p)))
print(ans)
