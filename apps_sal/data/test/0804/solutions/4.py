from collections import Counter

s = input()
c = Counter(list(s))
k = int(input())

if len(c.keys()) >= k:
	print(0)
elif len(c.keys()) < k <= len(s):
	print(k - len(c.keys()))
else:
	print('impossible')
