n = int(input())
l = list(map(int, input().split()))
k = 0
p = -1
for i in range(n):
	p = max(p, l[i])
	if p <= i + 1:
		k += 1
print(k) 

