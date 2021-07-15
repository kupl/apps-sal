n = int(input())
A = [0, 0, 0, 0, 0]
B = list(map(int, input().split(' ')))

for i in B:
	A[i] += 1

res = min(A[1], A[2])
A[1] -= res
A[2] -= res
A[3] += res

res += 2 * (A[1] // 3)
A[3] += A[1] // 3
A[1] %= 3

res += 2 * (A[2] // 3)
A[3] += 2 * (A[2] // 3)
A[2] %= 3

assert(A[1] == 0 or A[2] == 0)

if (A[1] == 1):
	if (A[3] > 0):
		res += 1 #; A[1] = 0; A[3] -= 1; A[4] += 1
	elif (A[4] > 1):
		res += 2 #; A[1] = 0; A[4] -= 2; A[3] += 3
	else:
		print(-1)
		return
elif (A[1] == 2):
	if (A[4] > 0):
		res += 2 #; A[1] = 0; A[4] -= 1; A[3] += 1
	elif (A[3] > 1):
		res += 2 #; A[1] = 0; A[3] -= 2; A[4] += 2
	else:
		print(-1)
		return

if (A[2] == 1):
	if (A[4] > 0):
		res += 1 #; A[4] -= 1; A[2] = 0; A[3] += 1
	elif (A[3] > 1):
		res += 2; #; A[2] = 0; A[3] -= 2; A[4] += 2
	else:
		print(-1)
		return
elif (A[2] == 2):
	res += 2 #; A[2] = 0; A[4] += 1
	
print(res)


