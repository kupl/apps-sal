n = int(input())
lst = list(map(int, input().split()))

free = [False] * 91

for x in lst:
	free[x] = True

not_false = 0
for i in range(1, len(free)):
	if free[i]:
		not_false = i
	else:
		if abs(i - not_false) >= 15:
			print(i)
			return
print(90)
