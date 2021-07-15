n = int(input())
left = {}
right = {}
for i in range(n):
	data = input()
	wk1 = 0
	wk2 = 0
	for j in data:
		if j == "(":
			wk1 += 1
		else:
			if wk1 == 0:
				wk2 += 1
			else:
				wk1 -= 1

	if (wk1 == 0):
		if not wk2 in left:
			left[wk2] = 0
		left[wk2] += 1
	if (wk2 == 0):
		if not wk1 in right:
			right[wk1] = 0
		right[wk1] += 1
	
#print(left, right)
ans = 0
for key in left:
	if key in right:
		ans += left[key] * right[key]

print(ans)



