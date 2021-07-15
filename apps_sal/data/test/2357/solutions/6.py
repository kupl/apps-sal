import sys
T = int(sys.stdin.readline())
for i in range(T):
	n = int(sys.stdin.readline())
	array = sys.stdin.readline().split(" ")
	lastSeen = [-10**6 for i in range(n + 1)]
	best = 10**6
	for j in range(len(array)):
		if j - lastSeen[int(array[j])] < best:
			best = j - lastSeen[int(array[j])]
		lastSeen[int(array[j])] = j
	if best == 10**6:
		print(-1)
	else:
		print(best + 1)
