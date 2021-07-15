h,w = map(int,input().split())
a = [[0]*w]*h

for i in range(h):
	a[i] = list(map(int,input().split()))

l = []
p = []
for i in range(h):
	if i%2 == 1:
		for j in reversed(range(w)):
			l.append(a[i][j])
			p.append((i+1,j+1))
	else:
		for j in range(w):
			l.append(a[i][j])
			p.append((i+1,j+1))
ans = []
i = 0
while i < h*w:
	if l[i]%2 == 1:
		k = i
		while ((k == i) or (l[k]%2 == 0)) and k < h*w - 1:
			ans.append(p[k]+p[k+1])
			k += 1
		i = k
	i += 1
print(len(ans))
for i in ans:
	print(*i)
