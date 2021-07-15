A, B = list(map(int, input().split()))

if A % 2 == 0:
	A_min = int(A * 12.5)
	A_max = A_min + 12
else:
	A_min = int(A * 12.5 + 0.5)
	A_max = A_min + 11

B_min = B * 10
B_max = B_min + 9

A_range = [n for n in range(A_min, A_max + 1)]
B_range = [n for n in range(B_min, B_max + 1)]

ans = -1

for n in A_range[::-1]:
	if n in B_range:
		ans = n
print(ans)

