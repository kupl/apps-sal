n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))

can_change = False
only_r_count = 0
only_b_count = 0
for i in range(n):
	if r[i] == 1 and b[i] == 0:
		only_r_count += 1
	elif b[i] == 1 and r[i] == 0:
		only_b_count += 1

if only_r_count == 0:
	print(-1)
else:
	print(only_b_count // only_r_count + 1)

