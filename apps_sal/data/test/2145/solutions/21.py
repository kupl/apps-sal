def reach(x, y):
	if x == 1:
		return y == 1
	if x == 2 or x == 3:
		return y < 4

	return True

for _ in range(int(input())):
	if reach(*map(int, input().split())):
		print("YES")

	else:
		print("NO")
