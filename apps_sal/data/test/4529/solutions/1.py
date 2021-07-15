from sys import stdin
input = stdin.readline
q = int(input())
N = 2342379478943
for rwwe in range(q):
	n = int(input())
	s = input()
	k = []
	for i in range(n):
		if s[i] == "L":
			k.append(1)
		if s[i] == "R":
			k.append(-1)
		if s[i] == "U":
			k.append(N)
		if s[i] == "D":
			k.append(-N)
	pref = [0] * (n+1)
	for i in range(1,n+1):
		pref[i] = pref[i-1] + k[i-1]
	#print(pref)############
	d = {}
	for i in pref:
		d[i] = []
	for i in range(len(pref)):
		d[pref[i]].append(i)
	best = 10000000000
	odp = ["a","a"]
	#print(d)##########
	for i in d:
		if len(d[i]) < 2:
			continue
		else:
			for j in range(1,len(d[i])):
				if d[i][j]-d[i][j-1] < best:
					best = d[i][j]-d[i][j-1]
					odp = [d[i][j-1]+1,d[i][j]]
	if odp != ["a","a"]:
		print(*odp)
	else:
		print(-1)

