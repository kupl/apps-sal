a = int(input())
s = list(input())
if a >26:
	print(-1)
else:
	b = set()
	for i in s:
		b.add(i)
	print(a-len(b))
		

