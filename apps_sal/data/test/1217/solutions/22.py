import bisect

n, m = map(int, input().split())
a = list(sorted(list(map(int, input().split()))))
b = list(map(int, input().split()))

r = []
for bb in b:
	i = bisect.bisect_right(a, bb)
	r.append(str(i))

print(' '.join(r))
