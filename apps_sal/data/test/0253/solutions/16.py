def solve(k):
	if min(k) > 3:
		print("NO")
		return

	x = [0, 0, 0]
	for x[0] in range(3):
		for x[1] in range(3):
			for x[2] in range(3):
				a = [False] * 15
				for i in range(3):
					j = 0
					while x[i] + j * k[i] < 15:
						a[x[i] + j * k[i]] = True
						j += 1
				is_possible = True
				for i in range(3, 15):
					is_possible = is_possible and a[i]
				if is_possible:
					print("YES")
					# print(" ".join(map(str, x)))
					return
	print("NO")

k = list(map(int, input().split()))
solve(k)



