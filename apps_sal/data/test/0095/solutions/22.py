n = int(input())
A = list(map(int,input().split()))
flag = 0
for i,a in enumerate(A):
	if i == 0:
		continue
	if flag == 0:
		if A[i - 1] < a:
			pass
		elif A[i - 1] == a:
			flag = 1
		else:
			flag = 2
	elif flag == 1:
		if A[i - 1] < a:
			flag = -1
			break
		elif A[i - 1] == a:
			pass
		else:
			flag = 2
	elif flag == 2:
		if A[i - 1] > a:
			pass
		else:
			flag = -1
			break
if flag >= 0:
	print("YES")
else:
	print("NO")
