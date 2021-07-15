
import sys

n, m, k = tuple(int(s) for s in sys.stdin.readline().split(" "))

filters = [ int(a) for a in sys.stdin.readline().split(" ") ]

if m <= k:
	print(0)
	return

count = 0
filters.sort(reverse=True)

for f in filters:
	k = k + f - 1
	count = count + 1
	if m <= k:
		print(count)
		return
else:
	print(-1)
