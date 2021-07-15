# import sys
# sys.stdin = open('cf596c.in')

from collections import namedtuple, defaultdict, Counter

Point = namedtuple("Point", "x y")

n = int(input())
pts = [Point(*list(map(int, input().split()))) for _ in range(n)]

have = Counter()
for pt in pts:
	have[pt.y - pt.x] += 1

ws = list(map(int, input().split()))
buckets = defaultdict(list)

for i, w in enumerate(ws):
	if have[w] == 0 or (
		(w == 0 and (len(buckets[1]) != len(buckets[0]) or (len(buckets[-1]) != len(buckets[0])))) or
		(w > 0 and ((len(buckets[w + 1]) != len(buckets[w])) or (len(buckets[w - 1]) != len(buckets[w]) + 1))) or
		(w < 0 and ((len(buckets[w - 1]) != len(buckets[w])) or (len(buckets[w + 1]) != len(buckets[w]) + 1)))
		):
		print('NO')
		return
	buckets[w].append(i)
	have[w] -= 1

ans = []
for w, bucket in list(buckets.items()):
	for x, i in enumerate(bucket, max(0, -w)):
		ans.append((Point(x, w + x), i))

ans.sort(key=lambda item: item[1])
print('YES')
print('\n'.join('%d %d' % pt for pt, i in ans))

