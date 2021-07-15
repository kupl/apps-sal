a = input()
b = input()
ans = {}
t = True
for i in range(len(a)):
	if a[i] in ans.keys():
		if ans[a[i]] != b[i]:
				t = False
	if b[i] in ans.keys():
		if ans[b[i]] != a[i]:
				t = False
	else:
		ans[a[i]] = b[i]
		ans[b[i]] = a[i]

if t:
	an = []
	for i in ans.keys():
		if i != ans[i] and i not in an and ans[i] not in an:
			an.append(i) 
			an.append(ans[i])
	print(len(an)//2)
	for i in range(0, len(an) - 1, 2):
		print(an[i], an[i + 1])
else:
	print(-1)
