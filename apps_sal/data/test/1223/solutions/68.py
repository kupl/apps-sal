n = int(input())
p = [int(i) for i in input().split()]

pos_list = [0] * n
for ind, i in enumerate(p):
	pos_list[i-1] = ind

left_nextInd = list(range(-1, n-1)) + [-1, -1]
right_nextInd = list(range(1, n+1)) + [n, n]

answer = 0
for i in range(1, n):
	ind = pos_list[i-1]
	l1 = left_nextInd[ind]
	l2 = left_nextInd[l1]
	r1 = right_nextInd[ind]
	r2 = right_nextInd[r1]

	answer += i * ((ind-l1) * (r2-r1) + (r1-ind) * (l1-l2))

	left_nextInd[r1] = l1
	right_nextInd[l1] = r1
print(answer)
