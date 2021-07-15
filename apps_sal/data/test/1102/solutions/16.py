n, a = [int(x) for x in input().split(' ')]

t = [0] + [int(x) for x in input().split(' ')]

m = min(n-a, a-1)

res = 0

if t[a] == 1:
	res += 1
	t[a] = 0

for i in range(1,m+1):
	s = t[a+i] + t[a-i]
	if s == 2: res += 2
	t[a+i],t[a-i] = 0, 0
	
print(res + sum(t))
