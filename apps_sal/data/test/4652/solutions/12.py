n = int(input())
for _ in range(n):
	_ = int(input())
	*l, = map(int, input().split())
	ans = False
	for i in range(len(l)-1):
		if l[i] == len(l):
			if not l[i+1] == 1:
				break
		else:
			if not l[i] + 1 == l[i+1]:
				break
	else:
		ans = True
	for i in range(len(l)-1):
		if l[i] == 1:
			if not l[i+1] == len(l):
				break
		else:
			if not l[i] - 1 == l[i+1]:
				break
	else:
		ans = True
	if ans:
		print("YES")
	else:
		print("NO")
