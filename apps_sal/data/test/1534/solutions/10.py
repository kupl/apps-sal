s = input()
le = len(s)
mx = 0
a = s.count('a')
b = s.count('b')
mx = max(mx, a)
mx = max(mx, b)
cnta = [0]*(le+1)
cntb = [0]*(le+1)
cnta[0] = 1 if s[0]=='a' else 0
cntb[0] = 1-cnta[0]

for i in range(1,le):
	cnta[i] = cnta[i-1]
	cntb[i] = cntb[i-1]
	if s[i] == 'a':
		cnta[i] += 1
	else:
		cntb[i] += 1

for i in range(le):
	for j in range(i+1, le):
		mx = max(mx, cnta[i]+b-cntb[i])
		mx = max(mx, cntb[i]+a-cnta[i])
		mx = max(mx, cnta[i]+cntb[j]-cntb[i]+a-cnta[j])
		
print(mx)

