Q = [int(x) for x in input().split(' ')]
n = Q[0]
k = Q[1]
M = Q[2]
D = Q[3]
m1=0

for i in range(D):
	m = n//(i*k+1)
	if m>M:
		m=M
	m1=max(m*(i+1),m1)

print(m1)

