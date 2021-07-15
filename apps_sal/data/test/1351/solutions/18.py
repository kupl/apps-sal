l, r = map(int, input().split())
from collections import Counter


for i in range(l, r + 1):
	s = str(i)
	c = Counter(s)
	if len(s) == len(c):
		print(i)
		return

print(-1)
