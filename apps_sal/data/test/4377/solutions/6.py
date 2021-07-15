l = list(map(int,input().split()))
k = max(l)
for i in l:
	if i != k:
		print(k - i, end = " ")
		
