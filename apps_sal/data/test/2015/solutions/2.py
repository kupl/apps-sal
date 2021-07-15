q = int(input())
for rwe in range(q):
	l = list(map(int,input().split()))
	l.sort()
	if l[2] <= l[0] + l[1] + 1:
		print("Yes")
	else:
		print("No")
