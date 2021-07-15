input()

s = set(map(int, input().split()))

if len(s) == 1:
	D = 0

elif len(s) == 2:
	D = max(s) - min(s)

	if D % 2 == 0:
		D = D // 2

elif len(s) == 3:
	lst = list(s)
	lst.sort()

	if lst[2] - lst[1] == lst[1] - lst[0]:
		D = lst[2] - lst[1]

	else:
		D = -1

else:
	D = -1

print(D)
