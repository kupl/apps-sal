n = int(input())
a = map(int, input().split())
b = set(a)
if len(b) <= 2:
	print("YES")
elif len(b) > 3:
	print("NO")
else:
	a = []
	for i in b:
		a.append(i)
	a.sort()
	if a[1] - a[0] == a[2] - a[1]:
		print("YES")
	else:
		print("NO")
