n = int(input())
visit = [0 for i in range(n+1)]
res = []
c = 0
s,t=0,0
def do(i):
	nonlocal c,s,t
	for j in range(i,n+1,2*i):
		res.append(i)
		c += 1
		if c >= (n-1) and n>2:
			if s == 0:
				s = j
			else:
				t = j
	return res
curr = 0
i = 1
while(i<=n):
	# print(i)
	do(i)
	i = 2*i
if n>2:
	res[n-1] = max(s,t)
# print(s,t)
for i in res:
	print(i,end=" ")
