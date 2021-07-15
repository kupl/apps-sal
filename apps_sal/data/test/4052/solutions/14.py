n = int(input())
s = input()
t = input()
a = []
for i in range(n):
	a.append(s[i])
s1 = dict()
t1 = dict()
for j in s:
	if j not in s1:
		s1[j] = 1
	else:
		s1[j] += 1
for j in t:
	if j not in t1:
		t1[j] = 1
	else:
		t1[j] += 1
if (s1 != t1):
	print(-1)
else:
	ans = []
	ind = 0
	while ind != n:
		q = ind
		while a[q] != t[ind]:
			q += 1
		while q != ind:
			a[q], a[q - 1] = a[q - 1], a[q]
			ans.append(q)
			q -= 1
		ind += 1
	print(len(ans))
	print(" ".join(map(str, ans)))	
			



