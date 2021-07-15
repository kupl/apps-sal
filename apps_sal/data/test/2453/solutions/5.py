n = int(input())
from collections import defaultdict, Counter
a = defaultdict(list)
count_left = Counter()
count_right = Counter()

for _ in range(n):
	l, r = map(int, input().split())
	count_left[l] += 1
	count_right[r] += 1

count = [0] * (n + 1)


pts = sorted(set(count_left.keys()) | set(count_right.keys()))
# pts.append(pts[-1])
c = 0
prev = pts[0]
for pt in pts:
	# print(prev, pt, c)
	if count_left[pt]:
		count[c] += pt - prev - 1		
		c += count_left[pt]
		count[c] += 1
		c -= count_right[pt]
	else:
		count[c] += pt - prev
		c -= count_right[pt]

	

	prev = pt
	# print(count)

print(' '.join(map(str, count[1:])))
