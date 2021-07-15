#fin = open("input.txt")
#n = int(fin.readline())
#s = list(fin.readline())
n = int(input())
s = list(input())
F = False
for k in range(1, (n + 3) // 4 + 1):
	for i in range(n - 3):
		#print(i)
		flag = True
		for j in range(5):
			#print(i + j * k + 1, end = " ")
			if i + j * k >= n or s[i + j * k] == ".":
				flag = False
		#print(flag)
		if flag:
			F = True
			break
	if F:
		break
if F:
	print("yes")
else:
	print("no")

