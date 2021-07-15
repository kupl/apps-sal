n,d = map(int,input().split())
arr = []
for i in range(d):
	arr.append(list(map(int,input().split())))
s = ""
for i in range(n):
	if i % 2 == 0:
		s = s + "0"
	else:
		s = s + "1"
print(s)
