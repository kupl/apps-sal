def move(rightmost, d, seq, current):
	plankno = seq[rightmost]
	# print(*seq)
	# while seq[rightmost] == plankno:
	moving = rightmost

	rem = rightmost-current-d
	rightmost += 1
	# print(rem)
	for i in range(rem):
		temp = seq[moving]
		seq[moving] = seq[moving-1]
		seq[moving-1] = temp
		moving -= 1


	# print(*seq, rightmost, moving)

	while rightmost != len(seq) and seq[rightmost] == plankno:
		seq[rightmost] = 0
		rightmost += 1

		seq[moving+1] = plankno
		moving += 1

	# print(*seq, moving, rightmost)
	return moving, rightmost


		# break




n, m, d = list(map(int, input().split()))
arr = [int(j) for j in input().split()]

planks = []
for i in range(m):
	planks += [i+1]*arr[i]

rem = [0]*(n-len(planks))
seq = rem + planks
# print(seq)
# print(rem, planks)

rightmost = n-1
while seq[rightmost] != 0 and rightmost != -1:
	rightmost -= 1

rightmost += 1
current = -1
# print(rightmost, current)

for i in range(m):
	if rightmost - current <= d:
		current = n-1
		break
	else:
		current, rightmost = move(rightmost, d, seq, current)


# print(n-current)
if n-current > d:
	print("NO")
else:
	print("YES")
	print(*seq)




