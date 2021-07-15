n, m = [int(i) for i in input().split()]
s = [[0, 0] for i in range(n)]
r = n**2
ans = []
q = 0
w = 0
for i in range(m):
	a, b = [int(y) for y in input().split()]
	if not s[a-1][0]:
		q+=1
	if not s[b-1][1]:
		w+=1
	s[a-1][0]+=1
	s[b-1][1]+=1
	ans.append(n**2-q*n-w*n+q*w)
print(*ans)

