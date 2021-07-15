n = int(input())
seq = list(map(int, input().split()))

if n == 1:
	print("no")
	return

pairs = []
cur = [-1, seq[0]]
fail = False

for i in range(1, len(seq)):
	cur[0], cur[1] = cur[1], seq[i]
	pairs.append([min(cur), max(cur)])

for x1, x2 in pairs:
	if not fail:
		for x3, x4 in pairs:
			if (x1 != x3 or x2 != x4) and (x1 < x3 < x2 < x4 or x3 < x1 < x4 < x2):
				fail = True
				break
	else:
		break

if fail:
	print("yes")
else:
	print("no")
