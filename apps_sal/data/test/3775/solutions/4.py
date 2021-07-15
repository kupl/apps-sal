def readpts():
	ip = list(map(int, input().split()))
	return [(min(ip[i], ip[i+1]), max(ip[i], ip[i+1])) for i in range(0,len(ip),2)]

N, M = list(map(int, input().split()))
pts1 = readpts()
pts2 = readpts()
#print(pts1)
#print(pts2)

def psb(a, b):
	if a == b: return False
	return any(i in b for i in a)

def sb(a, b):
	for i in a:
		if i in b:
			return i
	return -1 # should not happen

def ipsv(pts1, pts2):
	ans = False
	for p1 in pts1:
		gsb = set()
		for p2 in pts2:
			if psb(p1, p2):
				gsb.add(sb(p1, p2))
		if len(gsb) > 1: return False
		if len(gsb) == 1: ans = True
	return ans

def sv():
	gsb = set()
	for p1 in pts1:
		for p2 in pts2:
			if psb(p1, p2):
				gsb.add(sb(p1, p2))
	if len(gsb) == 0: return -1
	if len(gsb) == 1: return list(gsb)[0]
	if ipsv(pts1, pts2) and ipsv(pts2, pts1): return 0
	return -1

print(sv())

