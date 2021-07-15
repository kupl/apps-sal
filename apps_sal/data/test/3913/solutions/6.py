n = int(input())
s = input()

mp = dict()
st = [0]*n
k = 0
for i in s:
	if i.isalpha()==True:
		mp[i] = -1
	else:
		st[k] = 1
	k+=1

q = int(input())
tp = q
for i in range(q):
	s2 = input()
	cns = 0
	flag = 1
	for i in range(n):
		if s[i]!=s2[i] and not st[i]:
			tp-=1
			flag = 0
			break
		elif s2[i] in list(mp.keys()) and mp[s2[i]]==-1 and st[i]:
			tp-=1
			flag = 0
			break
	if flag :
		az = [0]*26
		for i in range(n):
			if s2[i] not in list(mp.keys()):
				mp[s2[i]]=1
				az[ord(s2[i])-97] = 1
			elif mp[s2[i]]!=-1 and not az[ord(s2[i])-97]:
				mp[s2[i]]+=1
				az[ord(s2[i])-97] = 1
cns = 0

for i in list(mp.keys()):
  if mp[i]==tp:
    cns+=1
print(cns)

