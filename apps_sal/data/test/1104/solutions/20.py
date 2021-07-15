import sys

def minp():
	return sys.stdin.readline().strip()
def mint():
	return int(minp())
def mints():
	return map(int,minp().split())

kk = [[[None]*4 for i in range(4)] for j in range(4)]
for i in range(4):
	for j in range(4):
		for k in range(4):
			z = None
			for x in range(4):
				if (i|x == j) and (i&x == k):
					z = x
			kk[i][j][k] = z

n = mint()
a = list(mints())
b = list(mints())
t = [0]*n
for i in range(4):
	t[0] = i
	ok = True
	for j in range(n-1):
		t[j+1] = kk[t[j]][a[j]][b[j]]
		if t[j+1] == None:
			ok = False
			break
	if ok:
		print("YES")
		print(*t)
		return
print("NO")
