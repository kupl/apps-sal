from collections import Counter

a = Counter(map(int, input().split()))
s = sum(b * c for b, c in a.items())
res = s

for b, c in a.items():
	if c >= 2:
		res = min(res, s - 2 * b)
	if c >= 3:
		res = min(res, s - 3 * b)

print(res)
