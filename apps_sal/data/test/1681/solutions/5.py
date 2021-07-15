import sys
#sys.stdin = open('input.txt', 'r')
n = input()
m = input()
N = dict()
M = dict()
for k in set(n):
	N.update({k : n.count(k)})
for k in set(m):
	M.update({k : m.count(k)})
S = 0
for k in M:
	if k in N:
		if N[k] >= M[k]:
			S += M[k]
		else:
			S += N[k]
	else:
		print(-1)
		return
print(S)

	

