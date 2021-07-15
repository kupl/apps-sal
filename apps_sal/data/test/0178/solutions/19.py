n = int(input())
s = str(input())
count = 0
p = []
for i in range(n):
	if s[i] == "8":
		count+=1
		p.append(i)
moves = int((n - 11)/2)
if moves >= count:
	print("NO")
	return
else:
	if p[moves] <= 2*moves:
		print("YES")
	else:
		print("NO")  


