a = list(map(int, input().split()))
k = 0
for c in a:
	k += c
if (k % 5 == 0) and (k > 0):
	print(int(k / 5))
else:
	print(-1)
